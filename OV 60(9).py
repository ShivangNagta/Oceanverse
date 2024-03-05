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


password='martin'

def vigenere_encrypt(s,password):
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new=''
    for i in range(len(s)):
        new+=a[((a.index(s[i]))+(a.index(password[i%(len(password))])))%26]
    return new

s=vigenere_encrypt(s,password)
k=6
'''

def letter_distributions(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    letters={}
    for i in s:
        if i in letters.keys():
            letters[i]+=1
        else:
            letters[i]=0
    return letters
ld=letter_distributions(s)


repeating_order=['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']       #most repeated letters in descending order taken from oxford's research paper
def cryptanalyse_substitution(s):      #Given that the string s is given to us and it is known that it was encrypted using some substitution cipher, predict the d
    d={}                             #dictionary which will return the subsituted letters    
    value_list=[]                    #list for taking the values of number of times all 26 letters(encrypted) have been repeated
    for i in ld.values():            #inserting that value in the list
        value_list.append(i)
    value_list.sort(reverse=True)
    for u in range(26):              #repeating loop for 26 letters
        for i in ld.keys():           #taking i as alphabets from ld's keys
            if ld[i]==value_list[u]:   #for u=0, which will give the most repeated value from the encrypted text, we will see which letter takes it
                d[repeating_order[u]]=i    #and assign it to e from the repeating_order list
                break       #breaking the loop if we find the correct pair 
            else:
                continue    
    return d


def letter(L):               #creating a funtion which returns 1 letter of the password taking a list as an argument
    new=''                    #empty string
    for i in range(len(L)):    #converting list to string
        new+=L[i]
    ld=letter_distributions(new)   #checking the distribution of letters in the string and taking the result in a dictionary
    num=list(ld.values())        #making list of the values of the dictionary
    num.sort(reverse=True)     #sorting in descending order
    a=num[0]                 #taking the highest value in variable 'a'
    b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  #list of letters
    for i in b:             #i taking all values from b in iteration
        if ld[i]==a:        #finding the most occuring letter in the encrypted text
            e=i             #assigning that letter to variable 'e'
    index=(b.index(e)-b.index('e'))%26      #finding the differnce between the encrypted letter and the true letter(most repeating) to get the index of key 
    return b[index]    #returning the 1 letter of key




def cryptanalyse_vigenere_afterlength(s,k):   
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''
    L=[]                     #empty list
    pswrd=''                  #empty password
    for i in s:               #appending all letters of encrypted text in the list L
        L.append(i)
    for u in range(k):        #Loop working k times
        L1=[]                 #empty list
        for i in range(len(L)):        #loop working of length of L times
            if ((k*i)+u)>=len(L):      #stopping loop if it exceeds the given loop 
                    break
            L1.append(L[(k*i)+u])      #appending values with interval of password length
        pswrd+=letter(L1)         #appending 1 letter of extracted key to password
    return pswrd
        
print(cryptanalyse_vigenere_afterlength(s,k))


