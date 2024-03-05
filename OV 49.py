def read():
    f=open("output.txt",'r')     #opens the file in read mode
    u=f.readline()               #u takes the first line as string
    while u:                     #loop runs til it's true
          print(u,end="")               #printing the string u
          u=f.readline()         #u takes the next line as string
    f.close()     
read()