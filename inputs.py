#!/usr/bin/env python3

import re


class UserInputs:
    """Requests inputs from user for search query"""

    def __init__(self):
        """
        states: list of all US states abbreviations
        jobs: list of job jobs
        locations: dict of each state mapped to its cities
        exp: specified experience level, None will include all jobs
        """
        self.states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        self.jobs = []
        self.locations = {}
        self.exp = None

    def get_jobs(self):
        return self.jobs

    def get_locations(self):
        return self.locations
    
    def get_exp(self):
        return self.exp

    @staticmethod
    def _clean_input(value):
        """Removes non-alpha symbols from input except space"""
        regex = re.compile("[^a-zA-Z ]")
        new_value = regex.sub("", value)
        return new_value

    @staticmethod
    def _process_string(value):
        """Replace space with + for Indeed query"""
        if " " in value:
            value = value.strip().replace(" ", "+")
        return value

    def input_jobs(self):
        """Get user inputs for job jobs and append to jobs list"""
        jobs = input("Enter all jobs: ")
        
        if not jobs:
            return

        # One job
        if "," not in jobs:
            jobs = self._clean_input(jobs)
            jobs = self._process_string(jobs)
            self.jobs.append(jobs)
            
        # Multiple jobs
        else:
            jobs = jobs.split(",")
            for job in jobs:
                job = self._clean_input(job)
                job = self._process_string(job)
                self.jobs.append(job)

    def input_states(self):
        """Get user inputs for all states"""
        states = input("Enter all states: ")

        if not states:
            print("Please enter the states you want to search in.")
            return

        # One state
        if "," not in states:
            states = states.upper()
            try:
                assert states in self.states, f"{states} is not a valid state."
            except AssertionError:
                return
            states = self._clean_input(states)
            self.locations[states] = []

        # Multiple states
        else:
            states = states.split(",")
            for state in states:
                state = self._clean_input(state)
                state = state.strip().upper()
                try:
                    assert state in self.states, f"{state} is not a valid state."
                except AssertionError:
                    return
                self.locations[state] = []
            
    def input_cities(self):
        """Get user inputs for all cities in each state"""
        for state in self.locations:
            cities = input(f"Enter all cities in {state}: ")

            if not cities:
                print("Please enter the cities of the states you want to search in.")
                return

            # One city
            if "," not in cities:
                cities = self._clean_input(cities)
                cities = cities.title()
                cities = self._process_string(cities)

                self.locations[state].append(cities)

            # Multiple cities
            else:
                cities = cities.split(",")
                for city in cities:
                    city = self._clean_input(city)
                    city = city.strip().title()
                    city = self._process_string(city)
                    self.locations[state].append(city)

    def input_exp(self):
        """Get user input for desired experience level"""
        exp = input("Enter experience level (entry/mid/senior): ")
        
        if not exp:
            return

        self.exp = self._clean_input(exp) + "_level"
