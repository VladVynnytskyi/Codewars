def descending_order(num):
    digits = list(str(num))
    
    sorted_digits = sorted(digits, reverse=True)
    
    joined_digits = "".join(sorted_digits)
    
    return int(joined_digits)

def descending_order(num):
    arr = list(str(num))
    nums = []
    for n in arr:
        nums.append(int(n))
    nums.sort()
    res= []
    for i in nums[::-1]:
        res.append(str(i))
    return int(''.join(res))
    