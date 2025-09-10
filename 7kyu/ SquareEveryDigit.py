def square_digits(nums):
    string_nums = str(nums)
    array_num = list(string_nums)
    square_numbers = []
    result = []
    for num in array_num:
        square_numbers.append(int(num) ** 2)
    for num in square_numbers:
        result.append(str(num))
    total = ''.join(result)
    return int(total)


def square_digits(nums):
    # Перетворюємо число у рядок, щоб дістати кожну цифру
    digits = str(nums)
    
    # Сюди будемо додавати квадрати цифр як рядки
    squared_digits = []

    # Підносимо кожну цифру до квадрату і додаємо в список
    for d in digits:
        square = int(d) ** 2
        squared_digits.append(str(square))
    
    # Об'єднуємо усі квадрати в один рядок і перетворюємо назад у число
    result = ''.join(squared_digits)
    return int(result)
