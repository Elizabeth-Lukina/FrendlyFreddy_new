import requests
from bs4 import BeautifulSoup


def get_pet_food_data(brand, food_type, pet_type):
    url = "https://www.petshop.ru/"
    params = {
        'brand': brand,
        'type': food_type,
        'pet': pet_type
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Ошибка при запросе: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Здесь вы должны определить, как найти товары на странице.
    # Например, предполагая, что товары находятся в элементе с классом 'product':
    products = soup.find_all(class_='product')  # Замените 'product' на истинный класс товара на сайте

    results = []

    for product in products:
        name = product.find(class_='product-name').text.strip()  # Проверить правильный класс
        weight = product.find(class_='product-weight').text.strip()  # Проверить правильный класс
        price = product.find(class_='product-price').text.strip()  # Проверить правильный класс

        results.append({
            'name': name,
            'weight': weight,
            'price': price
        })

    if results:
        print("Найденные товары:")
        for item in results:
            print(f"Название: {item['name']}, Вес: {item['weight']}, Цена: {item['price']}")
    else:
        print("Нет найденных товаров по заданным критериям.")


# Запрос на ввод у пользователя
brand_input = input("Введите бренд корма: ")
food_type_input = input("Введите тип корма (сухой/влажный): ")
pet_type_input = input("Для кого корм (кошка/собака): ")

get_pet_food_data(brand_input, food_type_input, pet_type_input)