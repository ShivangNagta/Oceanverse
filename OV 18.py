n=int(input("Number of Fibonacci digits to be printed:\n"))
a=0
b=1
new=0
for i in range(n):
    print(a)
    new=a+b
    a,b=b,new
   