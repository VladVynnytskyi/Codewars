def reverse_words(s):
    words = s.split()
    words.reverse()
    print(words)
    sent = ' '.join(words)
    return sent

reverse_words('Your like did fshd')