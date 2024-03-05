
import matplotlib.pyplot as p                #Importing matplotlib for plotting
import pandas as pd                          #Importing pandas for reading csv file
import numpy as np                           #Importing numpy for using polyfit function

f=pd.read_csv("C:\College\Python\SOCR-HeightWeight.csv")    #reading the csv file
x=f['Height(Inches)']                                       # assiging the column values of height to x
y=f['Weight(Pounds)']                                       # assiging the column values of weight to y
p.xlabel('Height(Inches)',fontsize=10)                      #Naming the x axis
p.ylabel('Weight(Pounds)',fontsize=10)                      #Naming the y axis
a, b = np.polyfit(x, y, 1)                 #Using the polyfit function to plot the line of best fit
p.plot(x,a*x+b)      
p.scatter(x,y,color='red')                 #Plotting the Height vs Weight scatter graph
p.show()                             #Printing the graph