s='tixawaxiwxbvxlkamqmynxlvq'
password='martin'

def vigenere_decrypt(s,password):
    '''decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new=''
    for i in range(len(s)):
        new+=a[((a.index(s[i]))-(a.index(password[i%(len(password))])))%26]
    return new

print(vigenere_decrypt(s,password))