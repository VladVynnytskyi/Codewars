def remove_smallest(numbers):
    result = []
    if len(numbers) != 0:
        for num in numbers:
            result.append(num)
        result.remove(min(result))
        return result
    else:
        return numbers
    

def remove_smallest(numbers):
    # якщо список порожній, повертаємо порожній список
    if not numbers:
        return []

    # створюємо копію, щоб не змінювати оригінал
    result = numbers.copy()

    # знаходимо індекс мінімального елемента
    min_index = result.index(min(result))

    # видаляємо елемент за індексом (лише перший мінімальний)
    del result[min_index]

    return result
