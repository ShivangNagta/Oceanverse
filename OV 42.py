def find_max():
    L=[]
    n=int(input("Enter the number of digits in the list:\n"))
    for i in range(n):                  #Appending n digits in the list L from the user
        A=int(input("Enter:\n"))
        L.append(A)
    return max(L)

print('Maximum digit is',find_max())