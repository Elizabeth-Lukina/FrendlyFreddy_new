import requests
from bs4 import BeautifulSoup

url = "https://www.petshop.ru/"
search_word = "собаки"  # слово, которое мы ищем

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    found = False  # Флаг для отслеживания, найдено ли слово
    for tag in soup.find_all(
            ['div', 'p', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):  # Проходим по всем текстовым тегам
        if search_word.lower() in tag.get_text().lower():  # Проверяем наличие слова в тексте тега
            print(f'Слово "{search_word}" найдено в теге: {tag.name}')  # Выводим название тега
            found = True  # Устанавливаем флаг в True, если слово найдено

            # Ищем все ссылки внутри найденного тега
            links = tag.find_all('a', href=True)
            for link in links:
                sub_url = link['href'] if link['href'].startswith('http') else url + link['href']
                sub_response = requests.get(sub_url)
                if sub_response.status_code == 200:
                    sub_soup = BeautifulSoup(sub_response.text, 'html.parser')
                    page_title = sub_soup.title.string if sub_soup.title else 'Без заголовка'
                    print(f'Переходим по ссылке: {sub_url}, Заголовок страницы: {page_title}')
                else:
                    print(f"Не удалось получить страницу по ссылке: {sub_url}")
            break  # Прерываем цикл, если слово найдено и обработаны ссылки

    if not found:
        print(f'Слово "{search_word}" не найдено на странице.')  # Сообщаем, если слово не найдено
else:
    print(f"Ошибка при запросе: {response.status_code}")  # Сообщаем об ошибке запроса