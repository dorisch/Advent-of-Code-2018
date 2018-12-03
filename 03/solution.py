"""
Created on Sun Dec  2 10:55:40 2018

@author: Dorota
"""
import re

data = open("data.txt").read().split("\n")

sq = {}
squ = {}
count = 0

for row in data:
    d = re.split('\D+', row)
    d.remove('')
    d1 = list(map(int,d))
    squ[d[0]] = []
    for w in range (d1[1]+1, (d1[1]+d1[3])+1):
        for h in range (d1[2]+1, (d1[2]+d1[4])+1):
            sq[str(w)+","+str(h)] = sq.get(str(w)+","+str(h) ,0)+1 #part1
            squ[d[0]].append(str(w)+","+str(h)) #part2

#part 1          
for val in sq.values():
    if val > 1:
        count = count +1

print(count)

#part 2
for k, s in squ.items():
    f = True
    for v in s:
        if sq[v] != 1:
            f = False
    if f:
        answer = k
            
print(answer) 
