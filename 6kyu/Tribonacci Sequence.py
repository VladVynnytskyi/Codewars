def tribonacci(signature, n):
    result = signature.copy()
    result_1 = []
    if n  > 3:
        for i in range(0, n - 3):
            result.append(result[i] + result[i+1] + result[i+2])
        return result
    else:
        for el in range(0, n):
            result_1.append(signature[el])
        return result_1


def tribonacci(signature, n):
    """
    Return the first n numbers of a tribonacci sequence that starts with `signature`.
    signature: list/tuple of 3 numbers, e.g. [a, b, c]
    n: non-negative integer
    """
    # Візьмемо рівно n стартових елементів (це покриває випадки n = 0, 1, 2, 3)
    seq = signature[:n]

    # Добудовуємо послідовність, поки не матимемо n елементів
    while len(seq) < n:
        seq.append(sum(seq[-3:]))

    return seq
