#!/usr/bin/env python3

from unittest.mock import patch
from unittest import TestCase
from inputs import UserInputs


class TestInputJobs(TestCase):
    
    def setUp(self):
        self.inputs = UserInputs()

    def tearDown(self):
        del self.inputs

    @patch("builtins.input", return_value="")
    def test_no_job(self, mock_input):
        self.inputs.input_jobs()
        test = []
        result = self.inputs.get_jobs()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="developer")
    def test_one_word_job(self, mock_input):
        self.inputs.input_jobs()
        test = ["developer"]
        result = self.inputs.get_jobs()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="junior developer")
    def test_multiple_words_job(self, mock_input):
        self.inputs.input_jobs()
        test = ["junior+developer"]
        result = self.inputs.get_jobs()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="developer, programmer, engineer")
    def test_multiple_job(self, mock_input):
        self.inputs.input_jobs()
        test = ["developer", "programmer", "engineer"]
        result = self.inputs.get_jobs()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="java developer, java engineer")
    def test_multipe_words_and_jobs(self, mock_input):
        self.inputs.input_jobs()
        test = ["java+developer", "java+engineer"]
        result = self.inputs.get_jobs()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="!#^%@%eng@%i%ne(_)(er")
    def test_invalid_job(self, mock_input):
        self.inputs.input_jobs()
        test = ["engineer"]
        result = self.inputs.get_jobs()
        self.assertEqual(test, result)


class TestInputStates(TestCase):

    def setUp(self):
        self.inputs = UserInputs()

    def tearDown(self):
        del self.inputs

    @patch("builtins.input", return_value="")
    def test_no_state(self, mock_input):
        self.inputs.input_states()
        test = {}
        result = self.inputs.get_locations()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="ga")
    def test_one_state(self, mock_input):
        self.inputs.input_states()
        test = {"GA": []}
        result = self.inputs.get_locations()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="il, tx, pa")
    def test_multiple_states(self, mock_input):
        self.inputs.input_states()
        test = {"IL": [], "TX": [], "PA": []}
        result = self.inputs.get_locations()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="n%$!z, v(&n,   !^%c%!ad")
    def test_invalid_states(self, mock_input):
        self.inputs.input_states()
        test = {}
        result = self.inputs.get_locations()
        self.assertEqual(test, result)


class TestInputCities(TestCase):

    def setUp(self):
        self.inputs = UserInputs()

    def tearDown(self):
        del self.inputs

    @patch("builtins.input", side_effect=["al", ""])
    def test_no_cities(self, mock_input):
        self.inputs.input_states()
        self.inputs.input_cities()
        test = {"AL": []}
        result = self.inputs.get_locations()
        self.assertEqual(test, result)

    @patch("builtins.input", side_effect=["tx", "dallas"])
    def test_one_city_one_state(self, mock_input):
        self.inputs.input_states()
        self.inputs.input_cities()
        test = {"TX": ["Dallas"]}
        result = self.inputs.get_locations()
        self.assertEqual(test, result)

    @patch("builtins.input", side_effect=["ca", "los angeles, san francisco"])
    def test_multiple_cities_one_state(self, mock_input):
        self.inputs.input_states()
        self.inputs.input_cities()
        test = {"CA": ["Los+Angeles", "San+Francisco"]}
        result = self.inputs.get_locations()
        self.assertEqual(test, result)

    @patch("builtins.input", 
           side_effect=["ga, nm, ny",
                        "atlanta",
                        "santa fe",
                        "new york city"])
    def test_one_city_multiple_states(self, mock_input):
        self.inputs.input_states()
        self.inputs.input_cities()
        test = {'GA': ['Atlanta'], 
                'NM': ['Santa+Fe'], 
                'NY': ['New+York+City']}
        result = self.inputs.get_locations()
        self.assertEqual(test, result)

    @patch("builtins.input", 
           side_effect=["va, fl, il", 
                        "richmond, virginia beach, alexandria", 
                        "miami, fort lauderdale", 
                        "chicago, rockford, arlington heights"])
    def test_multiples_cities_and_states(self, mock_input):
        self.inputs.input_states()
        self.inputs.input_cities()
        test = {"FL": ["Miami", "Fort+Lauderdale"],
                "IL": ["Chicago", "Rockford", "Arlington+Heights"],
                "VA": ["Richmond", "Virginia+Beach", "Alexandria"]}
        result = self.inputs.get_locations()
        self.assertEqual(test, result)


class TestInputExp(TestCase):

    def setUp(self):
        self.inputs = UserInputs()

    def tearDown(self):
        del self.inputs

    @patch("builtins.input", return_value="")
    def test_no_exp(self, mock_input):
        self.inputs.input_exp()
        test = None
        result = self.inputs.get_exp()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="entry")
    def test_entry_exp(self, mock_input):
        self.inputs.input_exp()
        test = "entry_level"
        result = self.inputs.get_exp()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="mid")
    def test_mid_exp(self, mock_input):
        self.inputs.input_exp()
        test = "mid_level"
        result = self.inputs.get_exp()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="senior")
    def test_senior_exp(self, mock_input):
        self.inputs.input_exp()
        test = "senior_level"
        result = self.inputs.get_exp()
        self.assertEqual(test, result)

    @patch("builtins.input", return_value="en!^$tr&^@#%$y")
    def test_invalid_exp(self, mock_input):
        self.inputs.input_exp()
        test = "entry_level"
        result = self.inputs.get_exp()
        self.assertEqual(test, result)
