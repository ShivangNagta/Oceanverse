


s=''
def textstrip(file_address,s):
    a=open(file_address,'r',errors="ignore")
    f=a.read()
    while f:
         for i in f:
             if i in 'abcdefghijklmnopqrstuvwxyz':
                s+=i
         f=a.read() 
    a.close()
    return s   
file='\College\Python\sherlock.txt'
s=textstrip(file,s)


password='ab'

def vigenere_encrypt(s,password):
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new=''
    for i in range(len(s)):
        new+=a[((a.index(s[i]))+(a.index(password[i%(len(password))])))%26]
    return new

s=vigenere_encrypt(s,password)


def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    s0=s
    sr=(" "*r)+s
    t=0
    for i in range(len(s)):
        if s0[i]==sr[i]:
            t+=1
        else:
            continue
    return t/len(s)









def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''
    i=0             #for initialising the rotation for the rotate_compare function
    prob=0          #initialising the probability of coincidence
    while prob<0.05:     #while loop 
        prob=rotate_compare(s,i+1)    #giving the probability found from rotate_compare function to variable 'prob'
        if prob>0.05:    #correct length found!
            k=i+1        #assigning the password length to k 
        else:            #loop working till correct length of password not found
            i+=1        
    return k              #returning the password length

print(cryptanalyse_vigenere_findlength(s))

