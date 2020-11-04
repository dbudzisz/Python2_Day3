#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#The code below was saved under test_cities.py. This file was used for unittest.

import unittest
from city_functions import city_country_pop1

class test_city_country(unittest.TestCase):
    """Tests for city_functions.py """

    def test_city_country(self):
        """Testing with no population"""

        result = city_country_pop1('Tacoma', 'United States')
        self.assertEqual(result, 'Tacoma, United States - population ')

    def test_city_country_population(self):
        """Testing with population"""
        result = city_country_pop1('Tacoma', 'United States', 200000)
        self.assertEqual(result, 'Tacoma, United States - population 200000')

unittest.main()

