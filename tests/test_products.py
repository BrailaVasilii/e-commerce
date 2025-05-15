from src.products import Product
from unittest import mock


def test_product_initialization():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_repr():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert (
        repr(product)
        == "Product(name=Samsung Galaxy S23 Ultra, price=180000.0, quantity=5)"
    )


def test_product_price_setter():
    product = Product("Test Product", "Test Description", 1500.0, 10)

    # Прямое повышение цены
    product.price = 2000.0
    assert product.price == 2000.0

    # Попытка снизить цену с использованием мока
    with mock.patch("builtins.input", return_value="y"):
        product.price = 1800.0
        assert product.price == 1800.0

    # Отмена снижения цены
    with mock.patch("builtins.input", return_value="n"):
        product.price = 1500.0
        assert product.price == 1800.0


def test_product_new_product(sample_products):
    """Тестирует метод new_product на создание или обновление продукта."""
    product_data = {
        "name": "Iphone 15",
        "description": "Updated Description",
        "price": 220000.0,
        "quantity": 5,
    }

    updated_product = Product.new_product(product_data, sample_products)
    assert updated_product.quantity == 13  # Обновлено количество
    assert updated_product.price == 220000.0  # Цена обновлена
