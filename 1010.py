# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 02:21:30 2019

@author: geekb
"""

line1 = input().split(" ")
line2 = input().split(" ")

i1, j1, k1 = line1
i1, j2, k2 = line2

total = (int(j1) * float(k1)) + (int(j2) * float(k2))

print("VALOR A PAGAR: R$ {0:.2f}".format(total,2))