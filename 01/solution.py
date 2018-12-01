# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:48:32 2018

@author: Dorota
"""

data = [int(x) for x in open("data_input.txt").read().split('\n')]

#First part of task
print(sum(data))

#Second part of task
list_of_sum = set()
suma = 0
x = True

while x:
    for i in data:
        suma = suma + i
        if suma in list_of_sum:
            x = False
            print(suma)
            break
        list_of_sum.add(suma)

