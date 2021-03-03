listL=['aha','nahu','shami','shadi']
count=0
for i in listL:
    for j in i:
        if j=='a':
            count=count+1
print("list is:",listL)
print("total number of a list is:",count)   