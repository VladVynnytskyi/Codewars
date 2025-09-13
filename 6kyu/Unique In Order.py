def unique_in_order(sequence):
    if len(sequence) >= 1:
        result = []
        result.append(sequence[0])
        for el in range(1, len(sequence)):
            if sequence[el] != sequence[el - 1]:
                result.append(sequence[el])
    else:
        return []
    return result


from typing import List, Sequence, TypeVar

T = TypeVar("T")

def unique_in_order(sequence: Sequence[T]) -> List[T]:
    """
    Повертає елементи послідовності без послідовних дублікатів,
    зберігаючи початковий порядок.
    Приклади:
      "AAAABBBCCDAABBB" -> ['A', 'B', 'C', 'D', 'A', 'B']
      [1, 2, 2, 3, 3]   -> [1, 2, 3]
    """
    if not sequence:
        return []

    result: List[T] = [sequence[0]]           # Беремо перший елемент
    for item in sequence[1:]:                 # Далі порівнюємо з останнім у result
        if item != result[-1]:
            result.append(item)

    return result
