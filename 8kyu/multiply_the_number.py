def multiply(n):
    digits = len(str(abs(n)))       
    res = n * 5 ** digits
    print(res)


multiply(int(input('Your number: ')))

#or

def multiply(n):
    digits = len(str(abs(n)))   # кількість цифр у числі
    return n * (5 ** digits)    # повертаємо результат
