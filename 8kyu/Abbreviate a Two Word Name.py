def abbrev_name(name):
    word = name.split()
    result = ''
    
    for i in word:
        result += i[0].upper()
    
    return ".".join(result)