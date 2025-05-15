import os
import tempfile
import json
from src.category import Category
from main import load_data_from_json


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Смартфоны"
    assert (
        sample_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(sample_category.get_products()) == len(sample_products)


def test_category_products(sample_category, sample_products):
    for product, sample in zip(sample_category.get_products(), sample_products):
        assert product.name == sample.name
        assert product.description == sample.description
        assert product.price == sample.price
        assert product.quantity == sample.quantity


def test_repr_category(sample_category):
    assert repr(sample_category) == "Category(name=Смартфоны, products=3)"


def test_load_data_from_json():
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy S23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        }
    ]

    # Создаем временный JSON-файл с тестовыми данными
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".json") as temp_file:
        json.dump(test_data, temp_file)
        temp_file.seek(0)

        # Тестируем функцию загрузки
        categories = load_data_from_json(temp_file.name)
        assert len(categories) == 1
        assert categories[0].name == "Смартфоны"
        assert len(categories[0].get_products()) == 3


def test_load_data_from_real_file():
    """Проверяем загрузку реального JSON-файла в проекте."""
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
    categories = load_data_from_json(file_path)
    assert len(categories) > 0
    assert categories[0].name == "Смартфоны"


def test_add_product(sample_category):
    from src.products import Product

    new_product = Product("Test Product", "Test Description", 1500.0, 10)
    sample_category.add_product(new_product)

    assert "Test Product, 1500.0 руб. Остаток: 10 шт." in sample_category.products
    assert len(sample_category.get_products()) == 4
