import string

def find_missing_letter(chars):
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    res = []
    
    for el in range(len(alphabet)):
        if alphabet[el] in chars:
            if alphabet[el - 1] not in chars:
                res.append(alphabet[el - 1])
    return res[1]