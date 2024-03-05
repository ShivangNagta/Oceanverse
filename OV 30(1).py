def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
a=int(input("Enter the larger number:\n"))
b=int(input("Enter the smaller number:\n"))
print("GCD is",gcd(a,b))