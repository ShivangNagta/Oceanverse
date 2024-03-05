n=int(input('Enter n:\n'))

def up(string):        #This function returns the same string which it takes as argument
    return string

def left(string):      #Function to rotate the inital pattern anticlockwise
    new=''             #To append the new pattern 
    for i in string:      
        if i=='D':
            new=new+'R'
        if i=='R':
            new=new+'D'
        if i=='U':
            new=new+'L'
        if i=='L':
            new=new+'U'
    return new            

def right(string):    #Function to rotate the intial pattern clockwise, also changing the starting point where it is required
    new=''
    for i in string:
        if i=='D':
            new=new+'L'
        if i=='R':
            new=new+'D'
        if i=='U':
            new=new+'R'
        if i=='L':
            new=new+'U'
                           #Since the top right pattern's inital point has to change from the inital one, so reversing the function
    new1=''                #Making the changes according to the new starting point
    for i in new:
        if i=='D':
            new1=new1+'U'
        if i=='R':
            new1=new1+'R'
        if i=='U':
            new1=new1+'D'
        if i=='L':
            new1=new1+'L'
    return new1            

def SFC(n):         #Recursion function to generate the higher level patterns from the smaller patterns
    if n==1:
        return 'DRU'
    else:
      return left(SFC(n-1))+'D'+up(SFC(n-1))+'R'+up(SFC(n-1))+'U'+right(SFC(n-1))

coordinates = [(1,1)]
direction = SFC(n)

for i in direction:
    x = coordinates[-1][0]
    y = coordinates[-1][1]
    if i == "D":
        coordinates.append((x,y+1))
    if i == "U":
        coordinates.append((x,y-1))
    if i == "R":
        coordinates.append((x+1,y))
    if i == "L":
        coordinates.append((x-1,y))
        
print(coordinates)