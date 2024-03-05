a=int(input("Enter your age:\n"))
if a<18 and a>0:
    print("You are a minor.")
elif a>17 and a<66:
    print("You are an adult.")
elif a>65:
    print("You are a senior citizen.")
else:
    print("Enter a valid age.")    