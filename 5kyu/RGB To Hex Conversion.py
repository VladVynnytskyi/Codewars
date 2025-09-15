def rgb(r, g, b):
    # Функція для обмеження значення від 0 до 255
    def clamp(x):
        if x < 0:
            return 0
        if x > 255:
            return 255
        return x

    # Обмежуємо значення і переводимо в HEX з двома символами
    return "{:02X}{:02X}{:02X}".format(clamp(r), clamp(g), clamp(b))