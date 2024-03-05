str=input("Enter the string you want to encrypt:\n")         
n=int(input("Write the number of shift in letters:\n"))
small='abcdefghijklmnopqrstuvwxyz'
capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new=''                        #for entering the encrypted string
for i in range(len(str)):       #loop for extracting every letter of string 
    if str[i] in small:          #encrypting if the letter is small
        new=new+small[(small.index(str[i])+n)%26]
    elif str[i] in capital:      #encrypting if the letter is capital
        new=new+capital[(capital.index(str[i])+n)%26]
    else:                      #adding the same string if it is a non letter character
        new=new+str[i]
print(new)