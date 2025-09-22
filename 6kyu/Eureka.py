def sumator(x):
    arr = list(str(x))
    i = 1
    res= []
    for n in arr:
        res.append(int(n) ** i)
        i +=1
    return sum(res)

def sum_dig_pow(a, b):
    nums = []
    res = []
    for num in range(a, b+1):
        nums.append(num)
            
    for num in nums:
        if num < 10:
            res.append(num)
        elif num == sumator(num):
            res.append(num)
    return res