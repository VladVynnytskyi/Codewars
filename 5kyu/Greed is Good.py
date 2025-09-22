from collections import Counter

def score(dice):
    counts = Counter(dice)
    res = 0
    
    # Triplets
    if counts[1] >= 3:
        res += 1000
        counts[1] -= 3
    for n in range(2, 7):
        if counts[n] >= 3:
            res += n * 100
            counts[n] -= 3
    
    # Singles
    res += counts[1] * 100
    res += counts[5] * 50
    
    return res
