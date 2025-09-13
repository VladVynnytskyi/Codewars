import string

def alphabet_position(text):
    result = []
    texts = text.lower()
    alphabet = list(string.ascii_lowercase)
    for let in texts:
        for num in alphabet:
            if let == num:
                result.append(str(alphabet.index(num) + 1))
    return ' '.join(result)