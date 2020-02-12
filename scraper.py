#!/usr/bin/env python3

from __future__ import with_statement
import csv
import os
import random
import requests
import sys
import time
from bs4 import BeautifulSoup
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
from inputs import UserInputs


class IndeedScraper:

    def __init__(self, jobs, locations, exp):
        self.jobs = jobs
        self.locations = []
        # Convert locations dict to list of query locations
        for state, cities in locations.items():
            for city in cities:
                self.locations.append(f"{city}&2C+{state}")
        self.exp = exp
        self.results = {}
        self.url = "https://www.indeed.com/"

    @staticmethod
    def _shorten_url(url):
        """
        Shorten job ad URL using tinyURL
        """
        request_url = ("http://tinyurl.com/api-create.php?" + urlencode({"url": url}))
        with contextlib.closing(urlopen(request_url)) as response:
            return response.read().decode("utf-8")

    @staticmethod
    def _remove_duplicates():
        """
        Remove duplicates from all job postings and delete old CSV file
        """
        with open ("all-postings.csv", "r") as in_file, open("job-postings.csv", "w") as out_file:
            exist = set()
            for job in in_file:
                if job in exist:
                    continue
                exist.add(job)
                out_file.write(job)
        os.remove("all-postings.csv")

    def write_csv(self, postings):
        """
        Write all job postings to CSV file
        """
        with open("all-postings.csv", "a") as csv_file:
            header = ["Job Title", "Company", "Location", "Salary" "Link"]
            writer = csv.writer(csv_file, dialect="excel")
            writer.writerow(header)

            for posting in postings:
                data = []

                # <a> tag for job title and link
                job = posting.find("a", class_="jobtitle")
                title = job.attrs.get("title")
                link = self._shorten_url(f"{self.url}{job.attrs.get('href')}")

                # Retrieves data value if item is not None
                company = posting.find("span", class_="company")
                if company is not None:
                    company = company.text.strip()
                location = posting.find("div", class_="recJobLoc")
                if location is not None:
                    location = location.attrs.get("data-rc-loc")
                salary = posting.find("span", class_="salaryText")
                if salary is not None:
                    salary = salary.text.strip()

                # Add all data to list and convert each item to str
                data.extend([title, company, location, salary, link])
                data = [str(i) for i in data]

                print(data)

                writer.writerow(data)

    def scrape(self):
        """
        Scrape all job postings from inputs
        """
        start = 0
        end = 0

        for job in self.jobs:
            for location in self.locations:
                query = f"{self.url}jobs?q={job}&l={location}&limit=50&sort=date&start={start}"

                # Add experience level to query if not None
                if self.exp is not None:
                    query += f"&explvl={self.exp}"

                page = requests.get(query)
                soup = BeautifulSoup(page.content, "html.parser")
                postings = soup.find_all("div", class_="jobsearch-SerpJobCard")

                # Find total number of jobs on first request
                if end == 0:
                    total = soup.find("div", id="searchCountPages").text.strip()

                    # Example string of total jobs -> "Page 1 of 2,193 jobs"
                    # Split the string, get 3rd element, and remove comma
                    total = total.split()[3]
                    if "," in total:
                        total = total.replace(",", "")
                    end = int(total)

                # Write job postings to CSV
                self.write_csv(postings)

                # If on last page, reset counters and go to next city, state
                if end - start < 50:
                    start = 0
                    end = 0
                    continue
                # Otherwise, go to next page
                else:
                    start += 50

                # Random delays
                time.sleep(random.randint(1, 10))

        # Write new file without duplicates
        self._remove_duplicates()
