# def search(array, number):
#     if number in array:
#         return array.index(number)
#     else:
#         return -1

def linear_search(array, number):          #лінійний пошук O(n)
    for num in range(0, len(array)):
        if num == number:
            return num
    return -1


def binary_search(array, number):
    middle_1 = len(array) / 2
    if array[middle_1] == number:
        return middle_1
    elif array[middle_1] < number:
        lenght = len(array) - middle_1
        middle_2 =  lenght / 2 
        if array[middle_2] == number:
            return middle_2
        


def binary_search(array, number):
    index = 0
    while number:
        