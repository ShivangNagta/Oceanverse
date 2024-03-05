
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



d={}
alpha='abcdefghijklmnopqrstuvwxyz'        #making a dictonary where every alphabet has been assigned value from a reverse dictionary
for i in range(len(alpha)):
        d[alpha[i]]=alpha[25-i]                              
def substitution_encrypt(s,d):
    new=''
    for i in s:        
        new+=d[i]        #concatenating the encrypted alphabet to a new empty string
    return new
s=substitution_encrypt(s,d)




def letter_distributions(s):
    letters={}
    for i in s:
        if i in letters.keys():
            letters[i]+=1
        else:
            letters[i]=1
    return letters
ld=letter_distributions(s)


repeating_order=['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']         #most repeated letters in descending order taken from oxford's research paper
def cryptanalyse_substitution(s):      #Given that the string s is given to us and it is known that it was encrypted using some substitution cipher, predict the d
    d={}                             #dictionary which will return the subsituted letters    
    value_list=[]                    #list for taking the values of number of times all 26 letters(encrypted) have been repeated
    for i in ld.values():            #inserting that value in the list
        value_list.append(i)
    value_list.sort(reverse=True)
    for u in range(26):              #repeating loop for 26 letters
        for i in ld.keys():           #taking i as alphabets from ld's keys
            if ld[i]==value_list[u]:   #for u=0, which will give the most repeated value from the encrypted text, we will see which letter takes it
                d[repeating_order[u]]=i   #and assign it to e from the repeating_order list
                break       #breaking the loop if we find the correct pair 
            else:
                continue    
    return d

print(cryptanalyse_substitution(s)) 


'''
def substitution_decrypt(s,d):                                                                             
    new=''                                        
    for i in s:                                               
        new+=d[i]        #concatenating the decrypted alphabet to a new empty string                                          
    return new                                        

print(substitution_decrypt(s,d)) 
 '''                                         