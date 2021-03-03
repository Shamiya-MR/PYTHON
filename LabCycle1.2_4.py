list1=[4,7,5,9]
list2=[2,4,6,3]
if(len(list1)==len(list2)):
    print("length of list1 and list2 are same")
else:
    print("length of list1 and list2 are not same")
if(sum(list1)==sum(list2)):
    print("sum of list1 and list2 are same")
else:
    print("sum of list1 and list2 are not same")
n=any(value in list2 for value in list1)
if(n==True):
    print("common value",end=" ")
    print(set(list2).intersection(set(list1)))
else:
    print("no common value")