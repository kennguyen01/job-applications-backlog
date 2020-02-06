#!/usr/bin/env python3

from inputs import UserInputs
from scraper import IndeedScraper


def main():
    user = UserInputs()
    user.input_jobs()
    user.input_states()
    user.input_cities()
    user.input_exp()

    jobs_scraper = IndeedScraper(user.get_jobs(), 
                                 user.get_locations(), 
                                 user.get_exp())
    jobs_scraper.scrape()


if __name__ == "__main__":
    main()