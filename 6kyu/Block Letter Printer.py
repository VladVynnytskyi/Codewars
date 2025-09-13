from preloaded import ALPHA  # dict: {'a': [...7 рядків...], ' ': [...]} 

def block_print(text: str) -> str:
    # 1) Нормалізація
    if not text:
        return ""
    text = text.strip()
    if not text:
        return ""
    text = text.lower()

    # 2) 7 порожніх рядків майбутнього банера
    rows = [""] * 7

    # 3) Додаємо символи по “гліфах”
    first_char = True
    for ch in text:
        # в умові — лише ASCII-літери та пробіли; на всякий випадок перевіряємо
        if ch not in ALPHA:
            continue

        glyph = ALPHA[ch]  # 7 рядків по 5 символів

        for i in range(7):
            if not first_char:
                rows[i] += " "           # рівно один пробіл між символами
            rows[i] += glyph[i]
        first_char = False

    # 4) Прибрати хвостові пробіли з кожного рядка
    rows = [line.rstrip() for line in rows]

    # 5) Повернути банер
    return "\n".join(rows)
