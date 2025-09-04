def century(year):
    if year % 100 == 0:
        century = year / 100
        return century
    else:
        century = year // 100
        return century + 1
    
def century(year):
    return (year + 99) // 100
