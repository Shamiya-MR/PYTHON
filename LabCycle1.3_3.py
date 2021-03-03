n1=float(input("enter 1st number:"))
n2=float(input("enter 2nd number:"))
n3=float(input("enter 3rd number:"))
large=0
if(n1>n2)and(n1>n3):
    large=n1
elif(n2>n1)and(n2>n3):

    large=n2
else:
    large=n3
print("largest number is",large)