d={}
alpha='abcdefghijklmnopqrstuvwxyz'        #making a dictonary where every alphabet has been assigned value from a reverse dictionary
for i in range(len(alpha)):
        d[alpha[i]]=alpha[25-i]
        
s='iamhuman'       
                          
def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    new=''
    for i in s:        
        new+=d[i]        #concatenating the encrypted alphabet to a new empty string
    return new

print(substitution_encrypt(s,d))
        
        
        
        