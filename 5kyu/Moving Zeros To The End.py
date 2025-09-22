def move_zeros(lst):
    for el in lst:
        if el == 0:
            lst.remove(el)
            lst.append(el)
    return 


def move_zeros(lst):
    # Крок 1: створюємо новий список для всіх елементів, які не є нулем
    result = []
    
    # Крок 2: рахуємо, скільки нулів у списку
    zero_count = 0
    
    # Крок 3: перебираємо всі елементи
    for x in lst:
        if x == 0:
            zero_count += 1      # якщо нуль — рахуємо його
        else:
            result.append(x)     # якщо не нуль — додаємо в результат
    
    # Крок 4: додаємо всі нулі в кінець
    for _ in range(zero_count):
        result.append(0)
    
    # Крок 5: повертаємо готовий список
    return result
