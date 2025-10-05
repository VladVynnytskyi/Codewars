def find_nb(m):
    sum = 0 
    n = 0
    while m >= sum:
        if m == sum:
            return n
        else:
            n += 1
            sum += n**3
    else: return -1
            