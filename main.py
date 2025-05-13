import os
import json
from src.products import Product
from src.category import Category


def load_data_from_json(file_path: str) -> list[Category]:
    """Загружает категории и продукты из JSON-файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    except json.JSONDecodeError:
        raise ValueError(f"Файл {file_path} содержит некорректный JSON.")

    categories = []
    for category_data in data:
        products = [
            Product(prod["name"], prod["description"], prod["price"], prod["quantity"])
            for prod in category_data["products"]
        ]
        category = Category(category_data["name"], category_data["description"], products)
        categories.append(category)

    return categories


if __name__ == "__main__":
    # Определяем путь к JSON-файлу
    file_path = os.path.join(os.path.dirname(__file__), "data", "products.json")

    # Загружаем данные из JSON
    categories = load_data_from_json(file_path)

    # Выводим данные
    for category in categories:
        print(f"Category: {category.name}, Number of Products: {len(category.products)}")
        for product in category.products:
            print(f" - Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
