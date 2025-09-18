def two_sum(numbers, target):
    res = []
    for el in range(0, len(numbers)):
        for i in range(1, len(numbers)):
            if numbers[el] + numbers[i] == target and el != i:
                res.append((el, i))
            if len(res) > 1:
                break
    return res[0]   


def two_sum(numbers, target):
    seen = {}   # тут ми зберігаємо числа, які вже бачили, разом з їхніми індексами
    for i, num in enumerate(numbers):   # йдемо по масиву: i - індекс, num - число
        diff = target - num             # різниця: яке число треба знайти, щоб у сумі дати target
        if diff in seen:                # якщо це число ми вже бачили
            return (seen[diff], i)      # повертаємо індекс того числа + поточний індекс
        seen[num] = i                   # якщо ні, то запам’ятовуємо це число і його індекс
