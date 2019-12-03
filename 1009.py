# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 02:17:47 2019

@author: geekb
"""

efn = input()
salary = float(input())
sales = float(input())

sales_c = sales * (15 / 100) # 15% Comission

total_in_month = sales_c + salary

print("TOTAL = R$ {0:.2f}".format(total_in_month,2))