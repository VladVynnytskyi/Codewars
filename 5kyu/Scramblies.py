def scramble(s1, s2):
    for char in set(s2):
        if s1.count(char) < s2.count(char):
            return False
    return True

from collections import Counter

def scramble(s1, s2):
    count1 = Counter(s1)   # рахуємо скільки разів кожна буква зустрічається у s1
    count2 = Counter(s2)   # рахуємо скільки разів кожна буква зустрічається у s2
    for char in count2:    # перебираємо всі букви, які є в s2
        if count2[char] > count1.get(char, 0):  
            # якщо у s2 букви більше, ніж у s1 → неможливо скласти
            return False
    return True             # якщо всі букви вистачає → можна скласти
