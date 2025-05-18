class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string.")
        if not len(name) >= 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        """Returns a list of all orders for this coffee."""
        from order import Order
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        """Returns a unique list of all customers who have ordered this coffee."""
        from order import Order
        customer_list = [order.customer for order in Order.all if order.coffee == self]
        return list(set(customer_list))

    def num_orders(self):
        """Returns the total number of orders for this coffee."""
        return len(self.orders())

    def average_price(self):
        """Returns the average price of all orders for this coffee."""
        order_list = self.orders()
        if not order_list:
            return 0
        total_price = sum(order.price for order in order_list)
        return total_price / len(order_list)