L=[2,-3,-7,4,5,8,-5,1]         #making a list for testing the program

#Using Kadane's Algorithm
def max(list):                  #taking a non empty list as argument
    max_sum=list[0]             #setting maximum sum to the 1st number of the list
    current_sum=0               #setting the current sum to o
    for i in list:              #running loop for every number in the list
        current_sum+=i                 #adding i to the current sum
        if max_sum>=current_sum:       #if the max sum is greater than the current sum then not updating it
            pass
        if max_sum<current_sum:        #if the max sum is lower than the current sum then, updating it
            max_sum=current_sum
        if current_sum>=i:             #if the current sum is greater than i then not updating it
            pass
        if current_sum<i:              #if the current sum is less than i, then resetting the current sum to i
            current_sum=i
    return max_sum              #returning the max sum

print(max(L))           