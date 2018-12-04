import re
from collections import Counter

data = open("data.txt").read().split("\n")

data = sorted(data, key=lambda d: re.split('\D+',d))

data = [i.split(" ") for i in data]

guards = {}
for n, i in enumerate(data):
    if i[2] == "Guard":
        ID = i[3]
        guards.setdefault(ID,[])
    else:
        guards[ID].append( int((i[1].split(":")[1]).replace("]","")) )

#part1
max = 0

for k, val in guards.items():
    suma = 0
    for i, v in enumerate(val):
        if i%2 == 1:
            suma = suma + (v-val[i-1])
            if suma > max:
                max = suma
                maxID = k

minutes = []
count = 0
for i,j in enumerate(guards[maxID]):
    if i%2 == 1:
        for v in range(guards[maxID][i-1], j):
            minutes.append(v)

print((Counter(minutes).most_common()[0])[0]*int(maxID.replace("#",""))) #answer1

#part 2
sleep = {}
count = 0
for k,val in guards.items():
    sleep[k] = []
    for i, j  in enumerate(val):
        if i%2 == 1:
            for v in range(guards[k][i-1], j):
                sleep[k].append(v)

sort_sleep = {}
for k, val in sleep.items():
    if val == []:
        continue
    else: sort_sleep[k] = (Counter(val).most_common()[0])

maks = 0

for k, val in sort_sleep.items():
    if maks < val[1]:
        maks = val[1]
        maks_time = (k,val)
print(int(maks_time[0].replace("#","")) * int(maks_time[1][0])) #answer2
