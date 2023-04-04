class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):

        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity = self.quantity - quantity
        else:
            raise ValueError("Товаров не хватает")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if not product.check_quantity(quantity):
            raise ValueError
        else:
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity

    def remove_product(self, product: Product, quantity=None):
        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products and quantity is None or quantity >= self.products.get(product):
            self.products.pop(product)
        else:
            self.products[product] = self.products.get(product) - quantity

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        get_total = 0
        for product in self.products:
            get_total += product.price * self.products[product]
        return get_total

    def buy(self):
        for product in self.products:
            if not product.check_quantity(self.products.get(product)):
                raise ValueError("Недостаточно товаров на складе")
            else:
                product.buy(self.products.get(product))
        self.products.clear()





