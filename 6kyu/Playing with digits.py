def dig_pow(n, p):
    arr_n = list(str(n))
    result = []
    for num in arr_n:
        result.append(int(num)** p)
        p += 1
    sum_result = sum(result)
    if sum_result % n == 0 :
        return sum_result / n
    else:
        return -1
    

def dig_pow(n: int, p: int) -> int:
    s = str(n)
    total = 0
    for i, ch in enumerate(s):
        digit = int(ch)
        total += digit ** (p + i)
    if total % n == 0:
        return total // n
    return -1
