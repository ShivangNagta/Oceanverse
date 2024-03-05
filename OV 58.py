n=int(input('Enter n:\n'))        #Taking input from the user

def up(string):                 #function which returns the original string
    return string
 
def up_rev(string):             #function which converts DRUL to ULDR
    new=''                      #empty string
    for i in string:            #loop working for all values of string
        if i=='D':
            new=new+'U'
        if i=='R':
            new=new+'L'
        if i=='U':
            new=new+'D'
        if i=='L':
            new=new+'R'
    return new                  #returning the new string


def down(string):               #function which converts DRUL to URDL
    new=''                      #empty string
    for i in string:            #loop working for all values of string
        if i=='D':
            new=new+'U'
        if i=='R':
            new=new+'R'
        if i=='U':
            new=new+'D'
        if i=='L':
            new=new+'L'
    return new
            
def down_rev(string):            #function which converts DRUL to DLUR
    new=''                       #empty string
    for i in string:             #loop working for all values of string
        if i=='D':
            new=new+'D'
        if i=='R':
            new=new+'L'
        if i=='U':
            new=new+'U'
        if i=='L':
            new=new+'R'
    return new


def peano(n):                #recursive program to return the pattern
    if n==1:                 #returning the pattern for n=1
        return 'UURDDRUU'
    else:                    #building up the recursion by using previous pattern for next pattern
      return up(peano(n-1))+'U'+down_rev(peano(n-1))+'U'+up(peano(n-1))+'R'+down(peano(n-1))+'D'+up_rev(peano(n-1))+'D'+down(peano(n-1))+'R'+up(peano(n-1))+'U'+down_rev(peano(n-1))+'U'+up(peano(n-1))
  
print(peano(n))