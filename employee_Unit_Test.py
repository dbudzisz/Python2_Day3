#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        #setting standard raise rate and salary
        self.default_raise = 0.02
        self.salary = 80000

        #instantiating the Employee class with default salary and raise rate
        self.my_raise = Employee('Dominick', 'Budzisz',self.salary, self.default_raise)

        #self.assertIn variable required a string for testing if output was there. default_raise1 is a formatted string used to search for the correct total salary during testing.
        self.default_raise1 = f'{(self.salary + (self.salary*self.default_raise)):,.2f}'

        #Other raise rates to test if multiple rates can be accepted.
        self.other_raise = [0.08, 0.1,0.9]

    def test_give_default_raise(self):
        self.assertIn(self.default_raise1, self.my_raise.get_info())

    def test_give_custom_raise(self):
        #for loop to pass the other raise rates

        for item in self.other_raise:
            self.default_raise = item
            self.assertIn(self.default_raise1, self.my_raise.get_info())




unittest.main()
    

