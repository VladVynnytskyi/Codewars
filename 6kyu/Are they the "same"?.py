def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    array1.sort()
    array2.sort()
    square = []
    for num in array1:
        square.append(num**2)
    square.sort()
    return  square == array2