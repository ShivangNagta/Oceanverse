d={}
alpha='abcdefghijklmnopqrstuvwxyz'        #making a dictonary where every alphabet has been assigned value from a reverse dictionary
for i in range(len(alpha)):
        d[alpha[i]]=alpha[25-i]
s='rznsfnzm'

def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    new=''
    for i in s:        
        new+=d[i]        #concatenating the decrypted alphabet to a new empty string
    return new

print(substitution_decrypt(s,d))