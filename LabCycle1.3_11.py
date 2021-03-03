def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=15
b=5
num=gcd(a,b)
print("gcd of",a,"and",b,"is:",num)
