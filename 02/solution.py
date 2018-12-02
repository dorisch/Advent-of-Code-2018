# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 10:55:40 2018

@author: Dorota
"""

#part 1
data = open("data.txt").read().split("\n")

c2 = 0 #initialize the counter for letters that occur twice
c3 = 0 #initialize the counter for letters that occur three times

for ID in data:
    counter = set()
    for char in ID:
        counter.add(ID.count(char))
    if 2 in counter and 3 in counter:
        c2 = c2 +1
        c3 = c3 +1
    elif 3 in counter:
        c3 = c3 +1
    elif 2 in counter:
        c2 = c2 +1

print(c2 * c3) #first answer

#part 2
def find_ID(data):
    for ID in data:
        for ID_comp in data:
            answer = []
            for i,j in zip(ID, ID_comp):
                if i == j:
                    answer.append(i)
            if len(answer) == (len(ID) - 1):
                get_ID = ID
                answer = "".join(answer)
                return answer
            
print(find_ID(data))
