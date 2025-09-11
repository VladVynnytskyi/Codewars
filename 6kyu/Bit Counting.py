def count_bits(n):
    bits_n = bin(n)[2:]
    array_bit = list(bits_n)
    result = 0
    for bit in array_bit:
        if bit == '1':
            result += 1
    return result



#or


def count_bits(n):
    return bin(n).count("1")
