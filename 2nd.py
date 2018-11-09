import pandas as pd


# load dataset
with open('forests.txt') as file:
    array2d = [[int(digit) for digit in line.split()] for line in file]


#1st scan
#Count frequence of each plant
frequence=[]
for j in range(1,207):
    count=0
    for i in range(len(array2d)):
        if j in array2d[i]:
            count=1+count
    frequence.append(count)

#Calculate Min support of our dataset of a threshold 50%
Min_Support=len(array2d)*0.5


#1st Cut
#Remove each pattern with a support less than the Min_Support
temp=[]
for i in range(len(frequence)):
    if frequence[i] >= Min_Support:
        temp.append(i+1)
frequence = temp

#This Function returns all the possibles set of all unique plants ID in a list
def poss(set,p):
    from itertools import combinations
    return [" ".join(map(str, comb)) for comb in combinations(set,p )]

#This Function returns a list with all patterns with a support greater or equal to the Min_Support
def counts(poss,orig):
    temp=[]
    output=[]
    for i in range(len(poss)):
        count = 0
        c = poss[i].split()
        for j in range(len(orig)):
            true = "true"
            for k in range(len(c)):
                if int(c[k]) not in orig[j]:
                    true="false"
            if true=="true":
                count=count+1
        temp.append([poss[i],count])
    df = pd.DataFrame(temp, columns=['item', 'freq'])

    for i in range(len(df.index)):
        if (df.freq[i]) >= Min_Support:
            output.append([df.item[i]])
    return output


#This Function Returns all unique plants ID from a list
def unique(dataset):
    container = []
    for i in range(len(dataset)):
        interval = str(dataset[i]).split()
        for j in range(len(interval)):
            if interval[j].isdigit():
                if interval[j] not in container:
                    container.append(interval[j])
    return container

#This Function returns a 1D array convert from a 2D array (in our example the returned type of the list Output is 2D)
def convertlist(list):
    converted=[]
    for i in range(len(list)):
        str1 = ''.join(list[i])
        c = str1.split()
        for k in range(len(c)):
            if c[k].isdigit():
                converted.append(c[k])
    return converted


converted=frequence
empty=1
output=[2,2,2]
s=1
while(len(output)>1 ):
    empty=0
    s=s+1
    frequence = (unique(converted))
    possibilities=poss(frequence,s)
    temp=counts(possibilities,array2d)
    if(len(temp)!=0):
        output=temp
    else:
        break
    converted=convertlist(output)

print("The max-frequent-plant species with the same support threshold:")
print(output)