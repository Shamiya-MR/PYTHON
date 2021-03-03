list=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    a=int(input("enter number:"))
    if a>100:
        list.append("over")
    else:
        list.append(a)
print(list)        