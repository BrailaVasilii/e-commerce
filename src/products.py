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
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """
        Сеттер цены. Реализует проверки перед установкой новой цены.

        :param new_price: Новое значение цены
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Подтверждение для снижения цены
        if new_price < self.__price:
            confirm = (
                input("Цена ниже текущей. Подтвердить снижение? (y/n): ")
                .strip()
                .lower()
            )
            if confirm != "y":
                print("Снижение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list["Product"] = None):
        """
        Класс-метод для создания нового продукта из словаря.

        :param product_data: Словарь с данными продукта
        :param existing_products: Список уже существующих продуктов
        :return: Объект Product
        """
        existing_products = existing_products or []

        for product in existing_products:
            if product.name == product_data["name"]:
                product.quantity += product_data["quantity"]
                product.__price = max(product.__price, product_data["price"])
                return product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __repr__(self):
        return (
            f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
        )
