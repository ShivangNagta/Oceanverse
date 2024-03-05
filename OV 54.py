L=[1,2,4,7,8,9,12,34,54]
n=int(input("Type the number to be searched:\n"))

def binary_search(L,n):       
    mid=L[len(L)//2]      #Selecting the middle element
    if mid==n:            #Returning the middle element if it is equal to n
        return 'Found'
    else:
        if mid>n:         #using recursion for the left part of the list
            if len(L)==1:        #if the element is not found till the end
                return 'Not Found'
            else:
                 return binary_search(L[:len(L)//2],n)
        elif mid<n:        #using recursion for the right part of the list
            if len(L)==1:
                return 'Not Found'
            else:
                 return binary_search(L[(len(L)//2):],n)

print(binary_search(L,n))