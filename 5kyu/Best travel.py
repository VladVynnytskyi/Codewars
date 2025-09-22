from itertools import combinations

def choose_best_sum(t, k, ls):
    if len(ls) < k:
        return None

    best = -1
    for combo in combinations(ls, k):
        total = sum(combo)
        if total <= t and total > best:
            best = total

    return best if best != -1 else None



from itertools import combinations as comb

def choose_best_sum(t, k, ls):
    res = 0
    if len(ls) < k:
        return 
    for com in comb(ls, k):
        s = sum(com)
        if s <= t and s > res:
            res = s
    if res == 0:
        return 
    return res
    
    