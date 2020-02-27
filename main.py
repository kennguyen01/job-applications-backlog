#!/usr/bin/env python3

import csv
from inputs import UserInputs
from scraper import IndeedScraper


def write_backlog(data):
    """Write job postings to CSV file"""
    total = 0

    with open("jobs-backlog.csv", "w", encoding="utf-8") as backlog:
        header = ["Job Title", "Company", "Location", "Salary", "Link", "Applied", "Interviewed", "Offered", "Rejected"]
        writer = csv.writer(backlog, dialect="excel")
        writer.writerow(header)

        for row in data:
            writer.writerow(row)
            total += 1
        
    print(f"{total} jobs added to backlog.")


def main():
    # Request inputs from user
    user = UserInputs()
    user.input_jobs()
    user.input_states()
    user.input_cities()
    user.input_exp()

    # Scrape jobs from Indeed
    jobs_scraper = IndeedScraper(user.get_jobs(), 
                                 user.get_locations(), 
                                 user.get_exp())
    jobs_scraper.scrape()

    # Write scraped jobs to CSV backlog
    jobs_data = jobs_scraper.get_results()
    write_backlog(jobs_data)


if __name__ == "__main__":
    main()