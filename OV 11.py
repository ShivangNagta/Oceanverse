n=int(input('Enter:\n'))
prime=True
if n<2:
    print("No Prime!")
else:
    for i in range(2,n+1):
        for t in range(2,i): #The loop doesn't work for i=2 so 2 is printed by default as prime remains true.
            if i%t==0:
               prime=False
        if prime==True:
            print(i)
        prime=True #Changing the value of prime to True in case it becomes False
        
