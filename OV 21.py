n=int(input("Enter the number whose factorial has to be calculated:\n"))
fac=1
for i in range(1,n+1):
    fac=fac*i    #Number from 1 to n keeps getting multiplied to fac with every loop
print("Factorial of",n,"is:\n",fac)