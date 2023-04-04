"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity_more(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(5000) is False

    def test_product_check_quantity_equal(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)

    def test_product_check_quantity_less(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(10)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1000)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(10001)
            assert pytest.raises(ValueError)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, 50)
            assert cart.products[product] == 50, 'Товар добавлен в корзину'
            cart.add_product(product, 50)
            assert cart.products[product] == 100, 'Количество товаров увеличилось'
            cart.add_product(product, 1500)
            assert pytest.raises(ValueError), 'Товаров недостаточно'

    def test_cart_remove_product(self, cart, product):
        cart.add_product(product, 150)
        cart.remove_product(product, 50)
        assert cart.products[product] == 100, 'Товары удалены'
        cart.remove_product(product, 50)
        assert cart.products[product] == 50, 'Товары удалены'
        cart.remove_product(product)
        assert cart.products.get(product) is None, 'Корзина пуста'

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 150)
        cart.clear()
        assert cart.products.get(product) is None, 'Корзина пуста'

    def test_cart_total_price(self, cart, product):
        cart.add_product(product, 150)
        assert cart.get_total_price() == 15000, 'Стоимость всех товаров'

    def test_cart_buy_greater(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, 1500)
            cart.buy()
            assert pytest.raises(ValueError), 'Товаров недостаточно'

    def test_cart_buy_equal(self, cart, product):
        cart.add_product(product, 1000)
        cart.buy()
        assert cart.products == {} and product.quantity == 0, 'Все товары проданы'

    def test_cart_buy_less(self, cart, product):
        cart.add_product(product, 150)
        cart.buy()
        assert cart.products == {} and product.quantity == 850, 'Часть товаров продана'