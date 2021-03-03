num=int(input("enter a number:"))
factorial=1
if num<0:
    print("factorial not found for negative numbers")
elif num==0:
    print("factorial of zerois",factorial)
else:
    for i in range(1,num+1):
        factorial=factorial*i
print("the factorial of",num,"is",factorial)