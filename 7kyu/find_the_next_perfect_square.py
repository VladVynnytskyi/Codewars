import math

def find_next_square(sq):
    res1 = math.sqrt(sq)
    if float(res1).is_integer():
        res2 = res1 + 1
        res3 = res2 * res2
        return res3
    else :
        return -1