def find_it(seq):
    for el in seq:
        if seq.count(el) % 2 != 0:
            print(el)
            return el


def find_it(seq):
    result = 0
    for el in seq:
        result = result ^ el
    return result
