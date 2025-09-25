def beeramid(bonus, price):
    amount = bonus// price
    level = 0
    result = []
    for cost in range(1,int(amount) + 1):
        if level + cost**2 <= amount:
            level += cost**2
            result.append(cost)
        else:
            break
    return result[-1] if result != [] else 0
