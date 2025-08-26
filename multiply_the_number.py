def multiply(n):
    digits = len(str(abs(n)))       
    res = n * 5 ** digits
    print(res)


multiply(int(input('Your number: ')))

#or

