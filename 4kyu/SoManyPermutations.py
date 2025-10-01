from itertools import permutations as pr

def permutations(s):
    all_perms = []                       
    for p in pr(s):                      
        word = ''.join(p)                 
        all_perms.append(word)
    unique_perms = set(all_perms)
    return list(unique_perms)
