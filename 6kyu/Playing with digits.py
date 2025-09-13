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