import random
n=int(input('Enter n:\n'))

def ok():                      #A function for appending n list in a list and then randomly adding n 'B''s in any nested list until all lists have atleast 1 'B;
    bin=[]
    t=0
    for i in range(n):
        bin.append([])
    for i in range(0,n):
        while len(bin[i])==0:
              bin[random.randint(0,n-1)].append('B')
              t=t+1
    return [bin,t]             #Returning the list as well as number of balls required to fill all the bins(t)

L=ok()
print(L[0],L[1])
