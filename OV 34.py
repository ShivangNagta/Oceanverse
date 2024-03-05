def factorial():
    n=int(input('Enter a number:\n'))
    a=1
    for i in range(1,(n+1)):                   
        a=a*i                                 #Multiplying the values (1 to n) in a(=1) by using loop
    return a                                  #Returning the factorial

print('Factorial is:',factorial()) 
        
        
    