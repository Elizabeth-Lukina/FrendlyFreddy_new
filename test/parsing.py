import requests
from bs4 import BeautifulSoup

url = "https://www.petshop.ru/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Пытаемся найти текст с фразой "товары дня"
    products_section = soup.find_all(string=lambda text: "товары дня" in text.lower())

    if products_section:
        for product in products_section:
            print(product.strip())  # Выводим текст, содержащий фразу "товары дня"
    else:
        print("Секция с 'товары дня' не найдена.")
else:
    print(f"Ошибка доступа к сайту: {response.status_code}")