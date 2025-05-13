class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация объекта продукта.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество продукта на складе
        """
        self.name = name  # Название продукта
        self.description = description  # Описание продукта
        self.price = price  # Цена продукта
        self.quantity = quantity  # Количество продукта

    def __repr__(self):
        """
        Возвращает текстовое представление объекта Product.

        :return: Строка с названием продукта, ценой и количеством
        """
        return (
            f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
        )
