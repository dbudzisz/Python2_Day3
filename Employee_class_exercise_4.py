#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee:
    def __init__(self, first_name, last_name, annual_salary, salary_raise=0.02):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__annual_salary = annual_salary
        self.__salary_raise = salary_raise


    def give_raise(self):
        #Calculates the total pay with the salary and raise

        annual_sal = float(self.__annual_salary)
        sal_raise = float(self.__salary_raise)
        total_pay = annual_sal + (annual_sal*sal_raise)

        return total_pay

    def get_info(self):
        return (f'Name:\t\t\t\t {self.__first_name} {self.__last_name}\n' +
               f'Annual salary:\t\t\t {self.__annual_salary:,.2f} \n' +
               f'Annual salary with raise:\t {self.give_raise():,.2f}')    
    

