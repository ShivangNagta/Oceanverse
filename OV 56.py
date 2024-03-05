def pop_arrange(lst , end ,start ): # function to take the last element from the list and separating bigger and smaller numbers around it
    pivot = lst[end] 
    while start < end: 
        if lst[start] > pivot: 
            lst.append(lst.pop(start)) 
            end -= 1 
        else: 
            start += 1 

    return start # return the correct position of pivot

def select(lst , start , end , k): # function to find kth smallest element
        pivot = pop_arrange(lst , end , start) 

        if pivot == k: 
            return float(lst[pivot]) 
        elif pivot > k: 
            return select(lst , start , pivot-1 , k) # call the function for the left part of pivot
        else: 
            return select(lst , pivot+1 , end , k) # call the function for the right part of pivot
   
        
def median(l): # function to find median
    if len(l)%2 == 1: # if length of list is odd
        return select(l , 0 , len(l)-1 , len(l)//2) # return the middle element
    else: # if length of list is even
        return ((select(l , 0 , len(l)-1 , (len(l)-1)//2) + select(l , 0 , len(l)-1 , len(l)//2)))/2 # return the average of middle two elements

L=[1,25,34,87,43,2,42,12]
print(median(L))