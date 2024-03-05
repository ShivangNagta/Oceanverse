a=input('Enter a string:\n')
b=input('Enter another string of same length:\n')
for i in range(len(a)):
    print(a[i]+b[i],end="") #for first loop it will concatenate first letter of a and b, then the 2nd letters in the 2nd loop and so on.