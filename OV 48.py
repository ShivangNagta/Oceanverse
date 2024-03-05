def txt():                          
    txt=open("outputs.txt",'w')                   #creating a file and opening in write mode
    n=int(input("Enter the number of natural numbers to be entered:\n"))   
    for i in range(n):        #loop for appending numbers in the file
        txt.write(str(i+1))
        txt.write('\n') 
    txt.close()
txt()