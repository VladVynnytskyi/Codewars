def order_weight(strng):
    weights = strng.split()
    dict_res = {}
    for weight in weights:
        sum = 0
        for num in weight:
            sum += int(num)
        dict_res[weight] = sum
    weights.sort()
    weights.sort(key = lambda x: dict_res[x])
    return ' '.join(weights)