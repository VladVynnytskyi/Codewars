def create_phone_number(n):
    part_1 = ''
    part_2 = ''
    part_3 = ''
    for num in n[0:3]:
        part_1 += str(num)
    for num in n[3:6]:
        part_2 += str(num)
    for num in n[6:10]:
        part_3 += str(num)
    
    return '(' + part_1 +') ' + part_2 + '-' + part_3
        
    


def create_phone_number(n):
    # Перетворюємо числа у рядки
    n = [str(num) for num in n]
    
    # Ділимо на частини
    part_1 = ''.join(n[0:3])
    part_2 = ''.join(n[3:6])
    part_3 = ''.join(n[6:10])
    
    # Форматуємо як телефонний номер
    return f"({part_1}) {part_2}-{part_3}"