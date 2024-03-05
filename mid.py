#creating function to turn the pattern(string)  anticlockwise

def left(pattern):    #defining the function, taking input a string
    new=''            #an empty string to append the new pattern
    for i in pattern:       # loop for changing the old pattern to the new one
        if i=='D':     #converting D to R
            new+='R'   
        if i=='R':     #converting R to D
            new+='D'
        if i=='U':     #converting U to L 
            new+='L'
        if i=='L':     #converting L to U
            new+='U'
    return new      #returning the new pattern as string


#creating function to turn the pattern(string) clockwise

def right(pattern):   #defining the function, taking input a string
    new=''            #an empty string to append the new pattern
    for i in pattern:  # loop for changing the old pattern to the new one
        if i=='D':     #converting D to L
            new+='L'
        if i=='R':     #converting R to D
            new+='D'
        if i=='U':     #converting U to R
            new+='R'
        if i=='L':     #converting L to U
            new+='U'
    new1=''          #another string to append the new reversed pattern 
    for i in new:     # loop for changing the old pattern to the new one
        if i=='D':     #converting D to R
            new1+='U'  
        if i=='R':     #not changing R
            new1+='R'
        if i=='U':     #converting U to D
            new1+='D'
        if i=='L':     #not changing L
            new1+='L'
    return new1     #returning the new string



#creating a function to return the original pattern

def up(pattern):       #function taking pattern(string) as argument
    return pattern     #returning the same pattern


#creating a function to return the pattern for desired value of n

def main(n):    #function taking n as input
    if n==1:       #returning the pattern for n=1
        return 'DRU'
    else:       #recursively calling the function using the previous pattern for printing the new one
        return left(main(n-1))+'D'+up(main(n-1))+'R'+up(main(n-1))+'U'+right(main(n-1))    #returning the updated pattern


#creating a function for converting the pattern to the list of tuples

def main_convert(pattern): #function taking the input of pattern(string)
    L=[(1,1)]          #list with inital position
    row=1              #initializing row
    column=1           #initializing column
    for i in pattern:  #taking all values of pattern
        if i=='D':             
            L.append((row+1,column))  #appending a tuple of new coordinates
            row=row+1                 #updating the row value
        if i=='U':
            L.append((row-1,column))  #appending a tuple of new coordinates
            row=row-1                 #updating the row value
        if i=='R':
             L.append((row,column+1)) #appending a tuple of new coordinates
             column=column+1          #updating the column value
        if i=='L':
            L.append((row,column-1))  #appending a tuple of new coordinates
            column-=1                 #updating the colmun value
    return L                       #returning the list of tuples


#Create a function SFC(n) which takes n as its input and returns the list
#of two tuples in the format of pattern.

def SFC(n):         #taking n as the arguemnt 
    pattern=main(n)     #calling the main function and returning the pattern to the variable pattern
    return main_convert(pattern) #returning the list pattern

#creating a function for converting the pattern to the list of tuples

def main_convert2(pattern,n): #function taking the input of pattern(string)
    L=[(2**n,1)]          #list with inital position
    row=2**n              #initializing row
    column=1           #initializing column
    for i in pattern:  #taking all values of pattern
        if i=='D':             
            L.append((row+1,column+1)) #appending a tuple of new coordinates
            row=row+1               #updating the row value
            column=column+1         #updating the column value
        if i=='U': 
            L.append((row-1,column-1))   #appending a tuple of new coordinates
            row=row-1               #updating the row value
            column-=1               #updating the column value
        if i=='R':
             L.append((row-1,column+1))   #appending a tuple of new coordinates
             column=column+1        #updating the colmun value
             row-=1                 #updating the row value
        if i=='L':
            L.append((row+1,column-1))    #appending a tuple of new coordinates 
            column-=1               #updating the colmun value
            row+=1                  #updating the row value
    return L                       #returning the list of tuples


#Create a function SFC(n) which takes n as its input and returns the list
#of two tuples in the format of pattern.

def SFC_Rotated(n):    #taking n as the argument
    pattern=main(n)    #calling the main function and returning the pattern the variable pattern
    return main_convert2(pattern,n)  #returning the pattern of list of tuples


n=int(input('Enter the value of n:\n'))            #taking n as the input from user
# print(SFC(n))                   #printing the SFC pattern 
print(SFC_Rotated(n))           #printing the rotated SFC pattern
