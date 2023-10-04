
def find_kth_smallest(L, k):
    while True:
        pivot = L[-1]
        lower = []
        higher = []
        for i in range(len(L) - 1):
            if L[i] > pivot:
                higher.append(L[i])
            else:
                lower.append(L[i])
        
        if k == len(lower) + 1:
            return pivot
        elif k <= len(lower):
            L = lower
        else:
            L = higher
            k -= len(lower) + 1

L = [110,23,3,2,1,34,67,97,32]
k = 6
result = find_kth_smallest(L, k)
print(result)
            
    


    
    
    
                   