import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    """Tests for the Coffee class"""

    def test_coffee_creation_valid(self):
        """Test creating a Coffee instance with a valid name."""
        coffee = Coffee("Espresso")
        assert coffee.name == "Espresso"

    def test_coffee_creation_name_too_short(self):
        """Test creating a Coffee with a name less than 3 characters."""
        with pytest.raises(ValueError) as excinfo:
            Coffee("AB")
        assert "Coffee name must be at least 3 characters long." in str(excinfo.value)

    def test_coffee_creation_name_not_string(self):
        """Test creating a Coffee with a non-string name."""
        with pytest.raises(TypeError) as excinfo:
            Coffee(123)
        assert "Coffee name must be a string." in str(excinfo.value)

    def test_coffee_name_immutable(self):
        """Test that the coffee name cannot be changed after initialization."""
        coffee = Coffee("Latte")
        with pytest.raises(AttributeError):
            coffee.name = "Cappuccino"

    def test_orders_empty(self):
        """Test orders() when there are no orders for this coffee."""
        coffee = Coffee("Mocha")
        assert coffee.orders() == []

    def test_orders_with_orders(self):
        """Test orders() when there are orders for this coffee."""
        coffee1 = Coffee("Espresso")
        customer1 = Customer("Alice")
        order1 = Order(customer1, coffee1, 3.50)
        order2 = Order(customer1, coffee1, 3.75)

        coffee2 = Coffee("Latte")
        Order(customer1, coffee2, 4.00)

        assert len(coffee1.orders()) == 2
        assert order1 in coffee1.orders()
        assert order2 in coffee1.orders()

    def test_customers_empty(self):
        """Test customers() when no customers have ordered this coffee."""
        coffee = Coffee("Mocha")
        assert coffee.customers() == []

    def test_customers_with_orders_unique(self):
        """Test customers() returns a unique list of customers."""
        coffee = Coffee("Espresso")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")

        Order(customer1, coffee, 3.50)
        Order(customer2, coffee, 3.75)
        Order(customer1, coffee, 3.60)  

        customers_who_ordered = coffee.customers()
        assert len(customers_who_ordered) == 2
        assert customer1 in customers_who_ordered
        assert customer2 in customers_who_ordered

    def test_num_orders(self):
        """Test num_orders() for a coffee."""
        coffee = Coffee("Espresso")
        customer1 = Customer("Alice")
        assert coffee.num_orders() == 0
        Order(customer1, coffee, 3.50)
        assert coffee.num_orders() == 1
        Order(customer1, coffee, 3.75)
        assert coffee.num_orders() == 2

    def test_average_price_no_orders(self):
        """Test average_price() when there are no orders."""
        coffee = Coffee("Espresso")
        assert coffee.average_price() == 0

    def test_average_price_with_orders(self):
        """Test average_price() calculates correctly."""
        coffee = Coffee("Espresso")
        customer1 = Customer("Alice")
        Order(customer1, coffee, 3.00)
        Order(customer1, coffee, 4.00)
        Order(customer1, coffee, 5.00)
        assert coffee.average_price() == pytest.approx(4.00)