a=input('Enter a string:\n')
v=0 # number of vowels
c=0 # number of consonants
L=['a','e','i','o','u']
for i in range(len(a)):
    if a[i] in L:
        v=v+1
    else:
        c=c+1 
print("Number of vowels in",a,"is",v)
print("NUmber of consonants in",a,"is",c)
    