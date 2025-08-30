def remove_exclamation_marks(s):
    word = list(s)
    while '!' in word:
        word.remove("!")
    sent = ''.join(word)
    return sent
