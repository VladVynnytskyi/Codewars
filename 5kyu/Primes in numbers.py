from math import sqrt

def prime_factors(n):
    factors = {}
    # шукаємо прості дільники до sqrt(n)
    for num in range(2, int(sqrt(n)) + 1):
        while n % num == 0:
            factors[num] = factors.get(num, 0) + 1
            n //= num
    
    # якщо залишилось просте число більше 1 — додаємо його
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    # будуємо рядок результату
    res = []
    for p in sorted(factors):
        k = factors[p]
        res.append(f"({p}**{k})" if k > 1 else f"({p})")
    
    return ''.join(res)


from math import sqrt

def prime_factors(n):
    dictionary_pimes = {}
    for num in range(2, int(sqrt(n))) :
        while n % num == 0:
            if num in dictionary_pimes:
                dictionary_pimes[num] += 1
                n = n // num
            else:
                dictionary_pimes[num] = 1
                n = n // num
    res = []
    if n == 1:
        for x, y in dictionary_pimes.items():
            if y != 1:
                res.append(f'({x}**{y})')
            else:
                res.append(f'({x})')
    else:
        for x, y in dictionary_pimes.items():
            if y != 1:
                res.append(f'({x}**{y})')
            else:
                res.append(f'({x})')
        res.append(f'({n})')
    return ''.join(res)