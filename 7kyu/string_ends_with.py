def solution(text, ending):
    lenght_ending = len(ending)
    lenght_text = len(text)
    result = lenght_text - lenght_ending
    substring = text[result:lenght_text]
#     if substring == ending:
#         return True
#     else:
#         return False
    return substring == ending

def solution(string, ending):
    return string.endswith(ending)