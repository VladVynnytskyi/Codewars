def wave(people):
    result = []
    for i in range(0, len(people)):
        if people[i] != ' ':
            result.append(people[:i] + people[i].upper() + people[i + 1:])
    return result    
        