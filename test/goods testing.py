import requests
from bs4 import BeautifulSoup


def get_pet_food_data(pet_type, food_type, brand):
    base_url = "https://www.petshop.ru"

    if pet_type.lower() == "собаки":
        category_url = "/catalog/dogs/"
    elif pet_type.lower() == "кошки":
        category_url = "/catalog/cats/"
    else:
        print("Неизвестный тип животного.")
        return

    url = base_url + category_url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все ссылки на продукты в категориях
    products = soup.find_all('a', {"class": "NavBar_menu_item__1a1+A"})
    for product in products:
        product_link = base_url + product['href']
        product_response = requests.get(product_link)
        product_soup = BeautifulSoup(product_response.text, 'html.parser')

        # Извлечение информации о товарах
        items = product_soup.find_all('div', {'class': 'ProductCard'})  # Убедитесь в правильности класса для товара
        for item in items:
            title = item.find('h2', class_='item-title').text if item.find('h2',
                                                                           class_='item-title') else 'Без названия'
            price = item.find('div', class_='ProductCard_content__price__16lF0').text if item.find('div', class_='ProductCard_content__price__16lF0') else 'Цена не указана'
            weight = item.find('span', class_='weight').text if item.find('span', class_='weight') else 'Вес не указан'
            print(f"Название: {title}, Цена: {price}, Вес: {weight}")


# Пример использования
pet_type_input = input("Введите тип животного (собаки/кошки): ").strip().lower()
food_type_input = input("Введите тип корма (сухой/влажный): ").strip().lower()
brand_input = input("Введите бренд корма: ").strip().lower()

get_pet_food_data(pet_type_input, food_type_input, brand_input)