# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 02:10:28 2019

@author: geekb
"""

number = int(input())
hour = int(input())
salary_hour = float(input())

count_salary = hour * salary_hour

print("NUMBER = {0}".format(number))
print("SALARY = U$ {0:.2f}".format(count_salary,2))