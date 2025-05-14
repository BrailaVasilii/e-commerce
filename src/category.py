from src.products import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса
    category_count = 0  # Количество созданных категорий (глобально для всего класса)
    product_count = 0  # Общее количество продуктов во всех категориях

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Инициализация объекта категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов, относящихся к категории
        """
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.products = products  # Список объектов Product

        # Увеличиваем счётчики для класса
        Category.category_count += 1
        Category.product_count += len(products)

    def __repr__(self):
        """
        Возвращает текстовое представление объекта Category.

        :return: Строка с названием категории и количеством продуктов
        """
        return f"Category(name={self.name}, products={len(self.products)})"
