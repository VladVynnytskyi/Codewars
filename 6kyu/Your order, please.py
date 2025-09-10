def order(sentence):
    array_words = sentence.split()
    array_corect = []
    for num in range(1, len(array_words) + 1):
        string_num = str(num)
        for word in array_words:
            if string_num in word:
                array_corect.append(word)    
    return ' '.join(array_corect)


def order(sentence):
    words_list = sentence.split()            # Розбиваємо речення на слова
    result_list = []                          # Сюди складатимемо слова у правильному порядку
    
    for position in range(1, len(words_list) + 1):  # Перебираємо позиції від 1 до кількості слів
        position_str = str(position)               # Перетворюємо номер у рядок для пошуку в словах
        for word in words_list:                    # Шукаємо слово з цією цифрою
            if position_str in word:
                result_list.append(word)           # Додаємо слово у правильному порядку
    
    return " ".join(result_list)                   # Збираємо всі слова у фінальне речення
