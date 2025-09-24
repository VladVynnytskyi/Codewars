from collections import Counter

def count(text):
    return dict(Counter(text))

#or

def count(string):
    count = {}
    for letter in string:
        if letter not in count: 
            count[letter] = 1
        else:
            count[letter] += 1
    return count

#or

def count(text):
    result = {}
    for letter in text:
        result[letter] = result.get(letter, 0) + 1
    return result
