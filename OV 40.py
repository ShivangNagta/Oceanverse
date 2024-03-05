

def spiral():            #Defining a function spiral
    c=''        #defining an empty string where we will be appending the spiral
    for i in range(1,1000000,2):  #making a loop which will work from 1 till 999999 with a gap of 2
        a='R'*i+'U'*i    #making a string whose iteration depends upon i
        b='L'*(i+1)+'D'*(i+1)  
        c=c+a+b        #appending the strings to c  
        if len(c)>1000000:    #breaking the loop when it exceeds 1000000 letters
            break
    return c         #Returning the spiral
spiral=spiral()    #Calling the function and putting the value of c in spiral
print(spiral[:1000000]) #printing 1000000 letters because spiral initially contained 1002056 letters.
print(len(spiral[:1000000]))