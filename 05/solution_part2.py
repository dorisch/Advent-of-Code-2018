# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:48:32 2018

@author: Dorota
"""

data = [x for x in open("data.txt").read().split('\n')]
data = list("".join(data[0]))


print(len(data))
#second part
sl = {}

data0 = data
data2 = [x.upper() for x in data]
da = set(data2)
minim = data

for x in da:
    sl[x] =[]
    dat = []
    i = 0
    flag = True
    for j,k in enumerate(data0):
        if x != k.upper():
            sl[x].append(k)
    data = sl[x]

    while flag and i < len(data) :
        if i != ((len(data))-1) and data[i].isupper() :
            if data[i+1] == data[i].lower():
                i = i+2
            
            else:
                dat.append(data[i])
                i = i+1
            
        elif i !=((len(data))-1) and data[i].islower():
            if data[i+1] == data[i].upper()  :
                i = i+2
            
            else:
                dat.append(data[i])
                i = i+1
            
        elif i == (len(data)-1) :
            dat.append(data[i])
            if len(data) == len(dat):
                flag = False
            else:
                data = dat
                dat = []
                i = 0
           
    if len(data)< len(minim):
        minim = data
        a = x

print(len(minim), a )


