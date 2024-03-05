def is_even(n):         #Defining a function which returns True value for even numbers.
    if n%2==0:
        return(True)

n=int(input("Enter an integer:\n"))
if is_even(n)==True:
    print("True")
else:
    print("False")