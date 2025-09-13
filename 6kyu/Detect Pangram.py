import string

def is_pangram(st):
    lower_st = st.lower()
    alphabet = list(string.ascii_lowercase)
    leters = []
    for word in lower_st:
        if word in alphabet:
            leters.append(word)
    unique_leters = list(set(leters))
    unique_leters.sort()
    return unique_leters == alphabet

import string

def is_pangram(st):
    alphabet = set(string.ascii_lowercase)
    letters = set()

    for ch in st.lower():
        if ch in alphabet:
            letters.add(ch)

    return letters == alphabet
