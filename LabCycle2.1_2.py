a=0
b=1
count=0
n=int(input("how many terms:"))
if n<=0:
    print("enter apositive number")
elif n==1:
    print("finocci series up to",n)
    print(a)
else:
    print("fibnocci series:")
while(count<n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count=count+1
