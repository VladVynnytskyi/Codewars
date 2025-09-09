def to_camel_case(text):
    result = []
    words = []
    split_words = text.split('_')
    for word in split_words:
        if '-' in word: 
            words.extend(word.split('-'))
        else:
            words.append(word)
    if not text:
        return ""
    else:
        for word in words:
            if word in words[0]:
                result.append(word)
            else:
                result.append(word.capitalize())
    return ''.join(result)