def partition(lst , end ,start = -1): # partition function
    pivot = lst[end] # pivot element
    while start < end: # loop to find the correct position of pivot
        if lst[start] > pivot: # if element is greater than pivot   
            lst.append(lst.pop(start)) # move it to the end of list
            end -= 1 # decrease the end
        else: # if element is smaller than pivot
            start += 1 # increase the start

    return start # return the correct position of pivot

def select(lst , start , end , k): # function to find kth smallest element
    if start < end:# if start is less than end
        pivot = partition(lst , end , start) # find the correct position of pivot

        if pivot == k: # if pivot is equal to k
            return float(lst[pivot]) # return the element at pivot
        elif pivot > k: # if pivot is greater than k
            return select(lst , start , pivot-1 , k) # call the function for the left part of pivot
        else: # if pivot is smaller than k
            return select(lst , pivot+1 , end , k) # call the function for the right part of pivot
    else: # if start is greater than end
        return None # return 0
        
def median(l): # function to find median
    if len(l)%2 == 1: # if length of list is odd
        return select(l , 0 , len(l)-1 , len(l)//2) # return the middle element
    else: # if length of list is even
        return ((select(l , 0 , len(l)-1 , (len(l)-1)//2) + select(l , 0 , len(l)-1 , len(l)//2)))/2 # return the average of middle two elements

if __name__ == "__main__":  # if the module is run directly
    x = [1, 4, 7, 5, 8, 57, 86, 743, 8, 73,56.5, 84]  # list to find median
    # printing the median of the list
    print(f"Median of following list is {median(x)}.")