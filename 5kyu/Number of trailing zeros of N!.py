def zeros(n):
    sum = 0
    i = 1
    while n//5**i >= 1:
        sum += n//5**i
        i += 1
    return sum
