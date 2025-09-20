def rot13(message):
    res = []
    for i in message:
        if i.isalpha() and i.islower():
                if ord(i) - 96 + 13 > 26:
                    char = ((ord(i) - 96 + 13) % 26) + 96
                    res.append(chr(char))
                else:
                    res.append(chr(ord(i)+ 13))
        elif i.isalpha() and i.isupper():
                if ord(i) - 64 + 13 > 26:
                    char = ((ord(i) - 64 + 13) % 26) + 64
                    res.append(chr(char))
                else:
                    res.append(chr(ord(i)+ 13))
        else:
            res.append(i)
    return ''.join(res)

import string

def rot13(message: str) -> str:
    table = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    )
    return message.translate(table)
