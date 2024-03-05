def fibonacci():
    n=int(input('Enter the fibonacci term number you desire:\n'))
    a=0
    b=1
    if n==1:                                  #to print to 1st term
        return a
    elif n==2:                                #to print the 2nd term
        return b
    else:                                     #to print the 3rd term and ownwards
        n=n-2
        for i in range(n):
            a,b=b,a+b
        return b                              
print(fibonacci())                             #Calling the function