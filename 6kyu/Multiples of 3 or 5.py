def solution(number):
    result = []
    for num in range(3, number):
        if num % 3 == 0 or num % 5 == 0:
            result.append(num)
    return sum(result)