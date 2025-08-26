def find_average(numbers):
    total = sum(numbers)
    if total != 0:
        res = total / len(numbers)
        return res
    else:
        return 0

