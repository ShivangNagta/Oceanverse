from OV_51 import bubble_sort                       #importing the function bubble_sort from OV_51.py
from OV52 import merge_sort                         #importing the function merge_sort from OV_52.py
from OV_53 import quick_sort                        #importing the function quick_sort from OV_53.py
from time import time                               #importing the function time from time module
from sys import setrecursionlimit as srl            #importing the function setrecursionlimit from sys module

with open("test.txt","r") as f:           #opening the file test.txt in read mode
    x = f.read().splitlines()[:10000]        #reading the file and storing the numbers in a list x

a = time()                  #calculating the time taken by each sorting algorithm
bubble_sort(x)              
b = time()
print((b-a))

a = time()
merge_sort(x)
b = time()
print((b-a))

srl(10**6)
a = time()
quick_sort(x)
b = time()
print((b-a))