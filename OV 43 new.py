import pandas as pda          #importing pandas to work with dataframes

capital=100000                #initialising capital value

df=pda.read_csv("C:\College\Python\Sensex.csv")        #reading the csv file as table
closing_value=df.iloc[:,-1]                          #extracting all the rows of last column
for i in range(len(closing_value)):                  #loop running for all given dates
    if i==7417:                                      #breaking the loop during the 4th last row
        capital=(capital/closing_value[i+1])*closing_value[i+3]         
        break
    if closing_value[i]>closing_value[i+1]:          #buying all the stocks if it is at local minima and selling when local maxima occurs
        if closing_value[i+1]>closing_value[i+2]:
            continue
        u=i+1
        while closing_value[u+1]<closing_value[u+2]:
            u=u+1
        capital=(capital/closing_value[i+1])*closing_value[u+1]
print("Hurray, you made a total of",capital,"rupees")               #printing the capital
        