def xo(s):
    s = s.lower()
    result_o = 0
    result_x = 0
    
    for char in s:
        if 'o' in char:
            result_o += 1
        if 'x' in char:
            result_x += 1
    if result_o == result_x:
        return True
    else :
        return False
        
def xo(s):
    s = s.lower()  # ігноруємо регістр
    count_o = s.count('o')
    count_x = s.count('x')
    return count_o == count_x

