def letter_distributions(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    letters={}
    for i in s:
        if i in letters.keys():
            letters[i]+=1
        else:
            letters[i]=0
    print(letters)


letter_distributions('fposdajgejwjepogfdaasdgfjowiebfkewjhfsdhfoeihwf')