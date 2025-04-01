import requests
from bs4 import BeautifulSoup

url = "https://www.petshop.ru/"
search_word = "собаки"  # слово, которое мы ищем

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    found = False  # Флаг, чтобы отслеживать, найдено ли слово

    for tag in soup.find_all():  # Проходим по всем найденным тегам
        text = tag.get_text()
        start = text.lower().find(search_word.lower())

        while start != -1:  # Пока мы находим вхождения
            found = True
            end = start + len(search_word)

            # Если тег имеет ссылку, переходим по ней
            link = tag.find('a', href=True)
            if link and link['href']:
                # Проверяем, чтобы ссылка открывалась в том же контексте
                sub_url = link['href'] if link['href'].startswith('http') else url + link['href']

                # Мы открываем ссылку только если найденное слово действительно присутствует в тексте
                if search_word.lower() in text.lower():
                    sub_response = requests.get(sub_url)
                    if sub_response.status_code == 200:
                        sub_soup = BeautifulSoup(sub_response.text, 'html.parser')
                        page_title = sub_soup.title.string if sub_soup.title else 'Без заголовка'
                        print(f'Переходим по ссылке: {sub_url}, Заголовок страницы: {page_title}')
                    else:
                        print(f"Не удалось получить страницу по ссылке: {sub_url}")

            start = text.lower().find(search_word.lower(), end)  # Продолжаем поиск

    if not found:
        print(f'Слово "{search_word}" не найдено на странице.')
else:
    print(f"Ошибка при запросе: {response.status_code}")