def high(x):
    dict_words = {}

    for word in x.split():
        score = 0  

        for letter in word:
            score += ord(letter) - 96

        dict_words[word] = score

    return max(dict_words, key=dict_words.get)
