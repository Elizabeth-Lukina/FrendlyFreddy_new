from collections import Counter


def decrypt_caesar(text, shift):
    decrypted_text = ""
    for char in text:
        if 'А' <= char <= 'Я':
            decrypted_char = chr((ord(char) - ord('А') - shift) % 32 + ord('А'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Оставляем символы, не входящие в диапазон
    return decrypted_text


def analyze_frequencies(text):
    # Убираем пробелы и считаем частоту букв
    text = text.replace(" ", "")
    frequency = Counter(text)
    return frequency


def find_best_shift(text):
    best_shift = -1
    highest_score = 0

    for shift in range(1, 33):
        decrypted = decrypt_caesar(text, shift)
        freq = analyze_frequencies(decrypted)

        # Сравниваем с типичной частотой букв
        score = sum(freq.get(char, 0) / len(decrypted) for char in 'ОЕАИНТ')

        if score > highest_score:
            highest_score = score
            best_shift = shift

    return best_shift


# Исходный текст
text = """\
ЬыыТввАывЩфвОсаРфыПцуУфы выЁыйСцуВыв фыЯвыСйуЙорАрвРцуАыфТыоСыл
выЯывСвцЙдлАыкВлоАотДоаСло длЕждНэж щшЫзщТгк зэОшгНре
шуОгшНгнЖврОгнЛраСип ынДовОнкКрп евЙпыИнаШраОнеРыиОитХвн нтЬвтТарАивСфыИраПра
"""

# Находим наилучший сдвиг
best_shift = find_best_shift(text)

# Расшифровываем с наилучшим сдвигом
if best_shift != -1:
    decrypted_text = decrypt_caesar(text, best_shift)
    print(f'Наилучший сдвиг: {best_shift}')
    print('Расшифрованный текст:', decrypted_text)
else:
    print("Правильный сдвиг не найден.")