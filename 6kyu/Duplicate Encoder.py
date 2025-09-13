def duplicate_encode(word):
    result = []
    words = word.lower()
    for char in words:
        if words.count(char) >= 2:
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)
            
from collections import Counter

def duplicate_encode(word: str) -> str:
    s = word.lower()
    freq = Counter(s)  # частоти кожного символу
    return ''.join('(' if freq[ch] == 1 else ')' for ch in s)
