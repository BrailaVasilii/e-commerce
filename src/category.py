from src.products import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса
    category_count = 0  # Количество созданных категорий (глобально для всего класса)
    product_count = 0  # Общее количество продуктов во всех категориях

    def __init__(self, name: str, description: str, products: list[Product] = None):
        """
        Инициализация объекта категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов, относящихся к категории
        """
        self.name = name
        self.description = description
        self.__products = products or []  # Приватный список продуктов

        # Увеличиваем счётчики для класса
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        """
        Добавляет продукт в категорию.

        :param product: Объект класса Product для добавления
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    def get_products(self) -> list[Product]:
        """
        Получение списка объектов Product.

        :return: Список продуктов
        """
        return self.__products

    @property
    def products(self) -> str:
        """
        Возвращает описание всех продуктов в категории.

        :return: Список продуктов в виде строк
        """
        return "\n".join(
            [
                f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
                for p in self.__products
            ]
        )

    def __repr__(self):
        return f"Category(name={self.name}, products={len(self.__products)})"
