def to_jaden_case(string):
    word = string.split()           #split() розділяє слова а list кожну букву
    total = []
    for i in range(0, len(word)):
        total.append(word[i].capitalize())
    return ' '.join(total)