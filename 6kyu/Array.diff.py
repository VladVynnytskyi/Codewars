def array_diff(a, b):
    for s in (0, len(a)):
        for el in b:
            for i in a:
                if el == i:
                    a.remove(i)
    return a


def array_diff(a, b):
    result = []            # Створюємо новий список для результату
    for element in a:       # Перебираємо всі елементи списку a
        if element not in b: # Якщо елемента немає у b
            result.append(element)  # Додаємо його в результат
    return result           # Повертаємо готовий список
