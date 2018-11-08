import pandas as pd
import numpy as np


# load dataset
with open('forests.txt') as file:
    array2d = [[int(digit) for digit in line.split()] for line in file]


frequence=[]

for j in range(1,207):
    count=0
    for i in range(len(array2d)):
        if j in array2d[i]:
            count=1+count
    frequence.append(count)
print(frequence)


#Min_Threshold=50% => 246/2 = 123

temp=[]
for i in range(len(frequence)):
    if frequence[i] > 123:
        temp.append(i+1)
frequence = temp
print(frequence)
temp=[]
z=0
t=1
item=""
for i in range(len(frequence)-1):
    z=t
    while(z<len(frequence)):
        if (frequence[i] != frequence[z]):
         item = str(frequence[i])+ " "+str(frequence[z])
         #item=item.split()
        if item not in temp:
            temp.append(item)
        z=z+1
    t=t+1
print(temp)
yo=[]
for j in range(len(temp)):
    count=0
    for i in range(len(array2d)):
        true="true"
        c = temp[j].split()
        for k in range(len(c)):
            if int(c[k]) not in array2d[i]:
                true="false"
        if true=="true":
            count=count+1
    yo.append(count)
print(yo)
frequence=yo

le=[]
for i in range(len(frequence)):
    if frequence[i] > 123:
        le.append(temp[i])
frequence = le
print(frequence)

