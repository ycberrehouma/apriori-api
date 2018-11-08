count=0
temp=[]
df = pd.DataFrame(columns=['item', 'count'])
z=1
while(z<len(frequence)):
    for i in range(len(frequence)):

        k = z
        while(k<(len(frequence))):
            count = 0
            for j in range(len(array2d)):
                if (frequence[i] in array2d[j]) and (frequence[k] in array2d[j]):
                    count = 1+count
            item = frequence[i], " ", frequence[k]
            df['item']=item
            df['count']=count
            k = k + 1
            print(df)


z=z+1
print("yo")
print(df)