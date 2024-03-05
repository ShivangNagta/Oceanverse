def quick_sort(L):  #Defining the function quicksort which takes the input as L
    low=[]          #For the elements whose elements are lower than the pivot point
    high=[]         #For the elements whose elements are higher than the pivot point
    if len(L)<2:   
        return L
    else:
        pivot=L.pop()
        for i in L:
            if i<=pivot:
                low.append(i)
            if i>pivot:
                high.append(i)
        return quick_sort(low)+[pivot]+quick_sort(high)   #recursing the program till the list is sorted and returning the sorted list
  
if __name__=='__main__':  
    n=int(input("Enter the total numbers to be sorted:\n"))  #Taking a list from user as input
    L=[]
    for i in range(n):
        L.append(int(input("Enter:\n")))
    print(quick_sort(L))