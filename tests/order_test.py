import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    """Tests for the Order class"""

    def test_order_creation_valid(self):
        """Test creating an Order with valid customer, coffee, and price."""
        customer = Customer("Test Alice")
        coffee = Coffee("Testpresso")
        price = 5.00
        order = Order(customer, coffee, price)

        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == price
        assert order in Order.all

    def test_order_creation_invalid_customer_type(self):
        """Test creating an Order with an invalid customer type."""
        coffee = Coffee("Test Latte")
        with pytest.raises(TypeError) as excinfo:
            Order("Not a Customer", coffee, 5.00)
        assert "Customer must be an instance of Customer class." in str(excinfo.value)

    def test_order_creation_invalid_coffee_type(self):
        """Test creating an Order with an invalid coffee type."""
        customer = Customer("Test Bob")
        with pytest.raises(TypeError) as excinfo:
            Order(customer, "Not a Coffee", 5.00)
        assert "Coffee must be an instance of Coffee class." in str(excinfo.value)

    @pytest.mark.parametrize("invalid_price, error_message_part, error_type", [
        (0.99, "Price must be between 1.0 and 10.0", ValueError),
        (10.01, "Price must be between 1.0 and 10.0", ValueError),
        ("5.00", "Price must be a float", TypeError),
        (None, "Price must be a float", TypeError),
    ])
    def test_order_creation_invalid_price(self, invalid_price, error_message_part, error_type):
        """Test creating an Order with invalid price (type or range)."""
        customer = Customer("Test Charlie")
        coffee = Coffee("Test Cappuccino")
        with pytest.raises(error_type) as excinfo:
            Order(customer, coffee, invalid_price)
        assert error_message_part in str(excinfo.value)

    def test_order_price_immutable(self):
        """Test that the order price cannot be changed after initialization."""
        customer = Customer("Test David")
        coffee = Coffee("Test Mocha")
        order = Order(customer, coffee, 7.50)
        with pytest.raises(AttributeError):
            order.price = 8.00

    def test_order_customer_property(self):
        """Test the customer property of an Order."""
        customer = Customer("Test Eve")
        coffee = Coffee("Test Americano")
        order = Order(customer, coffee, 3.00)
        assert order.customer == customer

    def test_order_customer_property_setter_type_check(self):
        """Test setting the customer property with type checking."""
        customer1 = Customer("InitCustomer")
        customer2 = Customer("NewCustomer") 
        coffee = Coffee("Test Coffee")
        order = Order(customer1, coffee, 5.00)

        order.customer = customer2
        assert order.customer == customer2

        with pytest.raises(TypeError) as excinfo:
            order.customer = "Not a Customer Instance"
        assert "Customer must be an instance of Customer class." in str(excinfo.value)

    def test_order_coffee_property(self):
        """Test the coffee property of an Order."""
        customer = Customer("Test Frank")
        coffee = Coffee("Test Flat White")
        order = Order(customer, coffee, 4.50)
        assert order.coffee == coffee

    def test_order_coffee_property_setter_type_check(self):
        """Test setting the coffee property with type checking."""
        customer = Customer("TestCustomer")
        coffee1 = Coffee("Init Coffee")
        coffee2 = Coffee("New Coffee")
        order = Order(customer, coffee1, 5.00)

        order.coffee = coffee2
        assert order.coffee == coffee2

        with pytest.raises(TypeError) as excinfo:
            order.coffee = "Not a Coffee Instance"
        assert "Coffee must be an instance of Coffee class." in str(excinfo.value)