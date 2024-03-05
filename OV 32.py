import random #importing random library to use randint function.
n=int(input("Enter a number for number of elements in the list:\n"))
L=[]
for i in range(1,n+1):
    L.append(random.randint(1,1000))
print(L)