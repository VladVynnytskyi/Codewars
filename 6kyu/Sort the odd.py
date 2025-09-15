def sort_array(source_array):
    odd = []
    for el in source_array:
        if el % 2 != 0:
            odd.append(el)
    odd.sort()
    for el in range(len(source_array)):
        if source_array[el] % 2 != 0:
            source_array[el] = odd.pop(0)
    return source_array