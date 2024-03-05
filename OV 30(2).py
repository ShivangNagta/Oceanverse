def gcd(m,u):                      #Defining a function to return a list giving i(number of times loop worked), and the 2 numbers
    i=0
    a=m
    b=u
    if a>b:
        while b>0:
            a,b=b,a%b            
            i=i+1
    return [i,m,u]
L=[0,0,0]
k=int(input("Enter number of digits:\n"))
for m in range(10**(k-1),10**(k)):             #2 loops for generating all possible pairs 
    for u in range(10**(k-1),10**(k)):
        if gcd(m,u)[0]>L[0]:                    #Searching for the loop which repeated the most
            L[0]=gcd(m,u)[0]                    
            L[1]=gcd(m,u)[1]                    #Replacing the numbers in list L's index 1 and 2, if they follow the above condition
            L[2]=gcd(m,u)[2]

print(L[1],L[2])
