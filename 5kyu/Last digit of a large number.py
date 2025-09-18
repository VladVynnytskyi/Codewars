def last_digit(n1, n2):
    if n2 == 0:
        return 1
    mod1 = n1 % 10
    res = []
    for i in range(1, n2+1):
        res.append((mod1 ** i)%10)
        if (mod1**(i+1))%10 in res:
            break
    return res[n2 % len(res) - 1]


def last_digit(n1, n2):
    return pow( n1, n2, 10 )
