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

    def __init__(self, jobs, states, cities, exp):
        self.jobs = jobs
        self.states = states
        self.cities = cities
        self.exp = exp

        self.url = "https://www.indeed.com/"
        self.limit = 50     # Max jobs per page
        self.start = 0
        self.max = 0        # Total jobs from query

    @staticmethod
    def _shorten_url(url):
        # Shorten job ad URL using tinyURL
        request_url = ("http://tinyurl.com/api-create.php?" + urlencode({"url": url}))
        with contextlib.closing(urlopen(request_url)) as response:
            return response.read().decode("utf-8")

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