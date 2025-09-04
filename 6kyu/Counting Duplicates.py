def duplicate_count(text):
    texts = text.lower()
    result = []
    for char in texts:
        if texts.count(char) >= 2:
            result.append(char)
    total = set(result)
    return len(total)
            
     