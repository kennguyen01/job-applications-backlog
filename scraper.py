#!/usr/bin/env python3

from __future__ import with_statement
import csv
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
        """Shorten job ad URL using tinyURL"""
        request_url = ("http://tinyurl.com/api-create.php?" + urlencode({"url": url}))
        with contextlib.closing(urlopen(request_url)) as response:
            return response.read().decode("utf-8")

    def write_csv(self, postings):
        """Write all job postings to CSV file"""
        with open("job-postings.csv", "a") as csv_file:
            fieldnames = ["Job Title", "Company", "Location" "Link", "Salary" "Applied", "Interviewed", "Rejected", "Offered"]
            writer = csv.DictWriter(csv_file, fieldnames)
            writer.writeheader()

            for posting in postings:
                data = []
                job = {}

                title = posting.find("a", class_="jobtitle")
                company = posting.find("span", class_="company")
                location = posting.find("div", class_="recJobLoc")
                link = self._shorten_url(f"{self.url}{title.attrs.get('href')[1:]}")
                salary = posting.find("span", class_="salaryText")


                data.extend([title, company, location, link, salary], [None]*4)
                for fieldname in fieldnames:
                    for item in data:
                        if item is None:
                            job[fieldname] = ""
                        else:
                            job[fieldname] = item

                writer.writerow(job)

    def scrape(self):
        """Scrape all job postings from inputs"""
        start = 0
        end = 0

        for job in self.jobs:
            for location in self.locations:
                query = f"{self.url}jobs?q={job}&l={location}&limit=50&explvl={self.exp}&start={start}"
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

    # def main(self):
    #     """
    #     Scrape Indeed job postings and write to csv file
    #     """
    #     while True:
    #         query = f"{self.url}jobs?q={self.titles}&l={self.cities}&2C+{self.states}&limit={self.max_job}&explvl={self.exp}&start={self.start}"
    #         page = requests.get(query)
    #         soup = BeautifulSoup(page.content, "html.parser")
    #         results = soup.find_all("div", class_="jobsearch-SerpJobCard")

    #         # Find total number of jobs on first request
    #         if END == 0:
    #             total = soup.find("div", id="searchCountPages").text.strip()
    #             total = total.split()[3]
    #             if "," in total:
    #                 total = total.replace(",", "")
    #             END = int(total)

    #         with open("jobs.csv", mode="a") as csv_file:
    #             fieldnames = ["Title", "Link", "Company", "Location", "Salary", "Applied", "Interviewed", "Rejected", "Offered"]
    #             writer = csv.DictWriter(csv_file, fieldnames)
    #             writer.writeheader()

    #             index = 0
    #             for result in results:
    #                 job = {}
    #                 title = result.find("a", class_="jobtitle")
    #                 job["Title"] = title.attrs.get("title")

    #                 link = _shorten_url(f"{URL}{title.attrs.get('href')[1:]}")
    #                 job["Link"] = link
                    
    #                 company = result.find("span", class_="company")
    #                 if company is None:
    #                     job["Company"] = ""
    #                 else:
    #                     job["Company"] = company.text.strip()
                    

    #                 location = result.find("div", class_="recJobLoc")
    #                 if location is None:
    #                     job["Location"] = ""
    #                 else:
    #                     job["Location"] = location.attrs.get("data-rc-loc")

    #                 salary = result.find("span", class_="salaryText")
    #                 if salary is None:
    #                     job["Salary"] = ""
    #                 else:
    #                     job["Salary"] = salary.text.strip()
                    
    #                 for k in ["Applied", "Interviewed", "Rejected", "Offered"]:
    #                     job[k] = ""

    #                 writer.writerow(job)
    #                 index += 1

    #         print(START, END)

    #         # Stop if on last page
    #         if END - START < 50:
    #             break
    #         else: 
    #             START += 50
                
    #         # Random delays
    #         time.sleep(random.randint(1, 10))