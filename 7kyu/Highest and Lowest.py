def high_and_low(numbers):
    nums = []
    result = []
    numbers = numbers.split(' ')
    for num in numbers:
        nums.append(int(num))
    result.append(str(max(nums)))
    result.append(str(min(nums)))
    
    return ' '.join(result)