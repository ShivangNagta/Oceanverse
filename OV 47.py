def matrix_multiplication(n):
    M1=[]                              
    M2=[]
    M3=[]
    
    for i in range(n):                         #for appending values from users in matrix 1 and also adding 0 in every place for matrix 3
        M1.append([])
        M3.append([])
        for u in range(n):
            M1[i].append(int(input('Enter(M1):\n')))
        for u in range(n):
            M3[i].append(0)
            
    for i in range(n):                         #for appending values from users in matrix 2
        M2.append([])   
        for u in range(n):
            M2[i].append(int(input('Enter(M2):\n')))
            
    for i in range(n):                         #Multiplying matricies
        for u in range(n):
            for k in range(n):
                M3[i][u]+=(M1[i][k])*(M2[k][u])
            
    print(M1)
    print(M2)
    print(M3)
    
n=int(input('Enter the order of matrix.\n'))      
matrix_multiplication(n)