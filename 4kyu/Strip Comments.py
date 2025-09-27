def strip_comments(strng, markers):
    arr = strng.split('\n')
    result = []
    for line in arr:
        new_line = ''
        for char in line:
            if char in markers:
                break
            new_line += char
        result.append(new_line.rstrip())

    return '\n'.join(result)