def binary_search_iterative(sor_list, x):       
    left = 0
    right = len(sor_list) - 1

    while left <= right:
        mid = (left+right)//2

        if sor_list[mid] == x:
            return mid
        elif sor_list[mid] < x:
            left = mid + 1
        elif sor_list[mid] > x:
            right = mid - 1




sort_list = [1, 2, 3, 4,5, 7, 8,10 ,11, 13, 15, 123, 1111]
x = 123
print(sort_list[binary_search_iterative(sort_list, x)])