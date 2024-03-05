start=100000                          #Initial amount that we have

import csv                            #Importing csv library for reading csv files
with open("C:\College\Python\Sensex.csv",'r') as f:     #reading csv file
    reader_object=csv.reader(f)                    #Returning iterable object which will iterate over lines in the given file
    head=[]
    head=next(f)
    sensex=[]                                      #Making a list to enter the date and closing values as tuples 
    for i in reader_object:
        sensex.append((i[0],float(i[-1])))         #Appending tuple of date and closing values
    f.close()                                  #Closing the file
    
min=[float(sensex[0][-1])]                  #Entering the first Closing value in list
t_min=[0]                                   #For entering the date of minimum closing value
t_max=[0]                                   #For entering the date of maximum closing value
max=[float(sensex[0][-1])]                  #Entering the first Closing value in list
for i in sensex:
    if float(i[-1])>=max[0]:                #For extracting the date and amount of min closing value
        max[0]=float(i[-1])
        t_max[0]=i[0]
    if float(i[-1])<=min[0]:                #For extracting the date and amount of max closing value
        min[0]=float(i[-1])
        t_min[0]=i[0]
        
stocks=start/min[0]
profit=((max[0])*stocks)-100000
print("Stocks should be bought on",t_min[0],'and sold on',t_max[0],'to make a total profit of Rupees',profit)