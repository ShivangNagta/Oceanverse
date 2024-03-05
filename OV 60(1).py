
def textstrip(file_address):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''
    a=open(file_address,'r',errors="ignore")
    f=a.read()
    while f:
         for i in f:
             if i in 'abcdefghijklmnopqrstuvwxyz':
                print(i,end='')
         f=a.read() 
    a.close()
    
file='\College\Python\sherlock.txt'
textstrip(file)