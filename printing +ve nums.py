lst=[]
lst2=[]
n=int(input("enter number of elements in the list: "))
for i in range(0,n):
    lst.append(int(input()))
    if(lst[i]>0):
        lst2.append(lst[i])
print(lst2)