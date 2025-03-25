import requests
from bs4 import BeautifulSoup

url = "https://www.petshop.ru/"
# Отправляем HTTP-запрос на указанный URL
response = requests.get(url)
# Проверяем, успешен ли запрос
if response.status_code == 200:
    print(200 )

    # Создаем объект BeautifulSoup для парсинга HTML-кода
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем все заголовки статей (предполагаем, что они находятся в теге h2)
    titles = soup.find_all('h5')
    search_word = 'Собаки'
    # Выводим заголовки статей
    for title in titles:
        print(title.get_text(strip=True))

    for tag in soup.find_all():
        # Проверяем, если слово есть в текстовом содержимом элемента
        if search_word.lower() in tag.get_text().lower():
            # Находим все вхождения слова и их позиции
            text = tag.get_text()
            start = 0

            while True:
                start = text.lower().find(search_word.lower(), start)
                if start == -1:
                    break
                end = start + len(search_word)
                print(f'Слово "{search_word}" найдено в теге <{tag.name}>: "{text[start:end]}" (позиция {start})')
                start += len(search_word)  # Продолжаем поиск с конца найденного слова


    # # Пытаемся найти текст с фразой "товары дня"
    # products_section = soup.find_all(string=lambda text: "товары дня" in text.lower())

    # if products_section:
    #     for product in products_section:
    #         print(product.strip())  # Выводим текст, содержащий фразу "товары дня"
    # else:
    #     print("Секция с 'товары дня' не найдена.")
else:
    print(f"Ошибка при запросе: {response.status_code}")
