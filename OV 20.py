n=int(input('Enter number of lines:\n'))
t=float(input('Enter curvature:\n'))
for i in range(n):                  #Loop will work for 'n' lines.
    if t>=0:                             #for right hand curve
        print(" "*int((((abs((n/2)-i)))**(2))*t)+'*')          #Giving gaps first in a way to generate a parabola looking curve(it's a parabola only for t=1), and then adding a star at the end.
    else:                                #for left hand curve
        print(" "*int(((n/2)**2)*abs(t)-(((abs((n/2)-i)))**(2))*abs(t))+'*')      #Reversing the curve using some idea of shifting of origin.