num = input("enter a number: ")
num = int(num)
first= 0
print(first)

second= 1
print(second)

for i in range(1,num-1):
    temp=first+second
    print(temp)
    first=second
    second=temp


