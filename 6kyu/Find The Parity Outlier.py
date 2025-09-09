def find_outlier(integers):
    even_numbers = []
    odd_numbers = []
    for number in integers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    if len(even_numbers) == 1:
        return even_numbers[0]
    else:
        return odd_numbers[0]