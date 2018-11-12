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
print("The Frequency of each number as fllow:")
print(frequence)

#Calculate Min support of our dataset of a threshold 50%
Min_Support=len(array2d)*0.5
Min_Confidence=0.7

print("Our Min Support for a threshold of 50% is eqaul to: ",Min_Support)
print("Our Min Confidence is equal to: ",Min_Confidence)

#1st Cut
#Remove each pattern with a support less than the Min_Support
temp=[]
for i in range(len(frequence)):
    if frequence[i] >= 172.2:
        temp.append(i+1)
frequence = temp
print()
print("Cut 1 of min threshold equal to 50%:")
print(frequence)

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
        if (df.freq[i]) >= 172.2:
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

#Return the number of times a pattern occur in the txt file
def occurence(pattern):
    count=0
    for i in range(len(array2d)):
        true = "true"
        for j in range(len(pattern)):
            if int(pattern[j]) not in array2d[i]:
                true="false"
        if true=="true":
            count=count+1
    return count


converted=frequence
empty=1
output=[2,2,2]
s=1
print()
print("Next cuts")
while(len(output)>1 ):
    empty=0
    s=s+1
    frequence = (unique(converted))
    print(len(frequence))
    print(frequence)
    possibilities=poss(frequence,s)
    print(possibilities)
    temp=counts(possibilities,array2d)
    if(len(temp)!=0):
        output=temp
    else:
        break
    print(output)
    print(len(output))
    converted=convertlist(output)
    print()
converted=convertlist(output)
for i in range(len(output)):
    zib = []
    converted = convertlist(output[i])
    zib = poss(converted, 3)
    print("-----")
    print("Association rules from", converted)
    for j in range(len(zib)):
        wa=[]
        c = zib[j].split()
        for k in range(len(c)):
            if c[k].isdigit():
                wa.append(c[k])
        x = [item for item in converted if item not in zib[j]]
        print(zib[j],"->" ,x[0])
        z=occurence(wa)
        g=occurence(converted)
        confidence=g/z
        print("confidence = #",converted," / ",wa," = ",z," / ",g," =" ,confidence)
        if confidence >= Min_Confidence:
            print("Therefore, it is a strong association rule")
        else:
            print("Not a strong association rule")
        print("----")




print("The pattern of all plant species (i.e., ids) in the forests with support  threshold = 50 is:")
print(output)