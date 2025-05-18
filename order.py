class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer class.")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class.")
        if not isinstance(price, float):
            raise TypeError("Price must be a float.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0, inclusive.")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be an instance of Customer class.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class.")
        self._coffee = value

from customer import Customer
from coffee import Coffee