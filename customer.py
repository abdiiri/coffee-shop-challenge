class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters, inclusive.")
        self._name = value

    def orders(self):
        """Returns a list of all orders placed by this customer."""
        from order import Order
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        """Returns a unique list of all coffees this customer has ordered."""
        from order import Order 
        coffee_list = [order.coffee for order in Order.all if order.customer == self]
        return list(set(coffee_list)) 

    def create_order(self, coffee, price):
        """Creates a new order for this customer."""
        from order import Order 
        from coffee import Coffee 
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of the Coffee class.")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Returns the Customer who has spent the most money on the given coffee.
        Returns None if the given coffee has not been ordered by any customer.
        """
        from order import Order
        from coffee import Coffee

        if not isinstance(coffee, Coffee):
            raise TypeError("Input must be a Coffee instance.")

        relevant_orders = [order for order in Order.all if order.coffee == coffee]
        if not relevant_orders:
            return None

        customer_spending = {}
        for order in relevant_orders:
            if order.customer in customer_spending:
                customer_spending[order.customer] += order.price
            else:
                customer_spending[order.customer] = order.price

        if not customer_spending:
            return None

        top_customer = sorted(customer_spending.items(), key=lambda item: item[1], reverse=True)[0][0]
        return top_customer