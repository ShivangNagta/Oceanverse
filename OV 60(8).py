'''
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
def vigenere_encrypt(s,password):
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new=''
    for i in range(len(s)):
        new+=a[((a.index(s[i]))+(a.index(password[i%(len(password))])))%26]
    return new
password='ab'
s=vigenere_encrypt(s,password)
'''

r=2

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

print(rotate_compare(s,r))
 
    