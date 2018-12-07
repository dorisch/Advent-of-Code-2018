# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 08:20:54 2018

@author: Dorota
"""

data = open("data.txt").read().split("\n")

for i, d in enumerate(data):
    data[i] = d.split("must be finished before step")
    data[i][0] = data[i][0].replace(" ","")
    data[i][0] = data[i][0].replace("Step","")
    data[i][1] = data[i][1].replace(" can begin.","")
    data[i][1] = data[i][1].replace(" ","")

key = set()
for k in data:
    key.add(k[1])

my_items = {}

for k in key:
    my_items[k] = []

for val in data:
    my_items[val[1]].append(val[0])

queue = []
   
for v in data:
    if v[0] not in list(key):
        my_items[v[0]] = []
        queue.append(v[0])
    
queue = list((sorted(queue))[0])

i = 0
while i < 1 +len(my_items.keys()):
    v_queue = []
    for key, val in my_items.items():
        result =  all(v in queue for v in val)
        if result:
            if key not in queue:
                v_queue.append(key)
    if len( v_queue) != 0:
        new_item = (sorted(v_queue)[0])
        queue.append(new_item)
        
    i = i+1

#solution to the first part of task:
print("".join(queue))
        
 
