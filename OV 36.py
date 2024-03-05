import random
n=int(input('Enter n:\n'))

def ok():                      #A function for appending n list in a list and then randomly adding n 'B''s in any nested list
    bin=[]
    for i in range(n):
        bin.append([])
    for u in range(n):
        bin[random.randint(0,n-1)].append('B')
    return bin

L=ok()
print(L) 

max=[0,0]                 #Extracting the data of maximum number of balls and the 1st bin in which it is present
for i in range(n):
    if len(L[i])>max[0]:
        max[0]=len(L[i])
        max[1]=i+1
print("Maximum Balls are",max[0],'and they are in bin',max[1])

