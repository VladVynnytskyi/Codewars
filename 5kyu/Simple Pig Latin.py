def pig_it(text):
    split_text = text.split()
    result = []  
    for word in split_text:
        if word.isalpha():                                          #isalfa() це функція яка перевіряє перевіряє, чи складається слово тільки з букв.
            result.append(word[1:] + word[0] + 'ay')
        else:
            result.append(word)

    return ' '.join(result)