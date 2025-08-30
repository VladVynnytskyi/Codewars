def positive_sum(arr):
    res = []
    for i in arr:
        if i > 0:
            res.append(i)
    return sum(res)  