def bubble_sort(L):                         #defining the function bubble_sort which takes the input as L    
    for j in range(len(L)-1):                #doing n-1 iterations
        for i in range(len(L)-1-j):#if the left number is larger than the right one, then exchanging their positions
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]
    return L

if __name__=='__main__':
            
    n=int(input('Enter the number of numbers to be sorted:\n'))    #taking the number of numbers to be sorted from user

    L=[]
    for i in range(n):                       #appending n numbers from user into list L
        L.append(int(input("Enter:\n")))
    print(L)
    print(bubble_sort(L))                   #printing the sorted list