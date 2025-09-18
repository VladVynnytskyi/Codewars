def increment_string(strng):
    if strng.isalpha() or strng == '':
        return strng + '1'
    letters = strng.rstrip('0123456789')
    digits = strng[len(letters):]
    digits = str(int(digits) + 1).zfill(len(digits))
    return letters + digits