def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = ''
    
    for i in string_:
        if i not in vowels:
            result = result + i
    return result
strd = 'Kello my liitghh auhs'
for i in strd:
    print(i)