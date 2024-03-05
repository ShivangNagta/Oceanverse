def merge(L1,L2):              #Defining a function to sort two given lists and returning the sorted list(new)
    new=[]
    i,j=0,0
    while i<len(L1) and j<len(L2):
        if (L1[i]<L2[j]):
           new.append(L1[i])
           i+=1
        else:
            new.append(L2[j])
            j+=1   
    new+=L1[i:]
    new+=L2[j:]
    return new
        
def merge_sort(L):       #Defining a recursive function which divides a list into two equal halves and then calls the mergee function to merge them
    if len(L)==1:
        return L
    else:
        mid=len(L)//2
        L1=L[:mid]
        L2=L[mid:]
        return merge(merge_sort(L1),merge_sort(L2))
    
    
if __name__ == "__main__":
    n=int(input('Enter the length of list:\n'))  #Taking a list as input from user
    L=[]
    for i in range(n):
        L.append(int(input('Enter number:\n')))
    print(merge_sort(L))

    