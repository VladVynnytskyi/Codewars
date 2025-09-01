def get_sum(a,b):
    tot = []
    if a == b:
        return a
    else:
        if a > b:
            for i in range(b, a+1):
                tot.append(i)
            return sum(tot)
        if b > a:
            for i in range(a, b+1):
                tot.append(i)
        return sum(tot)
            