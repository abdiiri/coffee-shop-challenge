import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    """Tests for the Customer class"""

    def test_customer_creation_valid(self):
        """Test creating a Customer with a valid name."""
        customer = Customer("Alice")
        assert customer.name == "Alice"

    def test_customer_name_setter_valid(self):
        """Test setting a valid name for a customer."""
        customer = Customer("Bob")
        customer.name = "Robert"
        assert customer.name == "Robert"

    @pytest.mark.parametrize("invalid_name, error_message_part", [
        ("", "between 1 and 15 characters"),
        ("ThisNameIsTooLong", "between 1 and 15 characters"),
    ])
    def test_customer_creation_name_invalid_length(self, invalid_name, error_message_part):
        """Test creating a Customer with name of invalid length."""
        with pytest.raises(ValueError) as excinfo:
            Customer(invalid_name)
        assert error_message_part in str(excinfo.value)

    def test_customer_creation_name_not_string(self):
        """Test creating a Customer with a non-string name."""
        with pytest.raises(TypeError) as excinfo:
            Customer(123)
        assert "Customer name must be a string." in str(excinfo.value)

    def test_customer_name_setter_invalid_length(self):
        customer = Customer("ValidName")
        with pytest.raises(ValueError) as excinfo:
            customer.name = "ThisNameIsFarTooLongForThisField"
        assert "between 1 and 15 characters" in str(excinfo.value)
        with pytest.raises(ValueError) as excinfo:
            customer.name = ""
        assert "between 1 and 15 characters" in str(excinfo.value)

    def test_customer_name_setter_invalid_type(self):
        customer = Customer("ValidName")
        with pytest.raises(TypeError) as excinfo:
            customer.name = 12345
        assert "Customer name must be a string." in str(excinfo.value)

    def test_orders_empty(self):
        """Test orders() when the customer has no orders."""
        customer = Customer("Charlie")
        assert customer.orders() == []

    def test_orders_with_orders(self):
        """Test orders() when the customer has orders."""
        customer1 = Customer("David")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        order1 = Order(customer1, coffee1, 3.00)
        order2 = Order(customer1, coffee2, 4.00)

        customer2 = Customer("Eve")
        Order(customer2, coffee1, 3.50)

        assert len(customer1.orders()) == 2
        assert order1 in customer1.orders()
        assert order2 in customer1.orders()

    def test_coffees_empty(self):
        """Test coffees() when the customer has ordered no coffees."""
        customer = Customer("Frank")
        assert customer.coffees() == []

    def test_coffees_with_orders_unique(self):
        """Test coffees() returns a unique list of coffees ordered."""
        customer = Customer("Grace")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")

        Order(customer, coffee1, 3.00)
        Order(customer, coffee2, 4.00)
        Order(customer, coffee1, 3.50)

        coffees_ordered = customer.coffees()
        assert len(coffees_ordered) == 2
        assert coffee1 in coffees_ordered
        assert coffee2 in coffees_ordered

    def test_create_order(self):
        """Test create_order() successfully creates and returns an Order."""
        customer = Customer("Heidi")
        coffee = Coffee("Cappuccino")
        price = 5.00

        order = customer.create_order(coffee, price)
        assert isinstance(order, Order)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == price
        assert order in Order.all
        assert order in customer.orders()

    def test_create_order_invalid_coffee_type(self):
        """Test create_order() with an invalid coffee type."""
        customer = Customer("Ivan")
        with pytest.raises(TypeError) as excinfo:
            customer.create_order("Not a Coffee", 4.00)
        assert "Coffee must be an instance of the Coffee class." in str(excinfo.value)

    def test_most_aficionado_no_orders_for_coffee(self):
        """Test most_aficionado when the coffee has no orders."""
        coffee_no_orders = Coffee("Unordered Special")
        customer1 = Customer("Mallory") 
        Order(customer1, Coffee("Popular Blend"), 5.00)
        assert Customer.most_aficionado(coffee_no_orders) is None

    def test_most_aficionado_one_customer(self):
        """Test most_aficionado with one customer for the coffee."""
        coffee = Coffee("Espresso")
        customer1 = Customer("Alice")
        Order(customer1, coffee, 3.50)
        Order(customer1, coffee, 3.75)
        assert Customer.most_aficionado(coffee) == customer1

    def test_most_aficionado_multiple_customers(self):
        """Test most_aficionado with multiple customers."""
        coffee = Coffee("Latte")
        alice = Customer("Alice")
        bob = Customer("Bob")
        charlie = Customer("Charlie")

        Order(alice, coffee, 4.00)
        Order(bob, coffee, 3.00)
        Order(bob, coffee, 3.50)  
        Order(charlie, coffee, 5.00) 

        assert Customer.most_aficionado(coffee) == bob

    def test_most_aficionado_tie_returns_first_by_implementation(self):
        """Test most_aficionado in case of a tie (based on typical sort stability or first encountered)."""
    
        coffee = Coffee("TieCoffee")
        customer_a = Customer("Andy")
        customer_b = Customer("Brenda")

        Order(customer_a, coffee, 5.00)
        Order(customer_b, coffee, 5.00)

        o1 = Order(customer_a, coffee, 5.00)
        o2 = Order(customer_b, coffee, 5.00)

        aficionado = Customer.most_aficionado(coffee)
        assert aficionado in [customer_a, customer_b]

        Order.all = []
        Order(customer_a, coffee, 5.00)
        Order(customer_b, coffee, 5.01)
        assert Customer.most_aficionado(coffee) == customer_b


    def test_most_aficionado_invalid_coffee_type(self):
        """Test most_aficionado with an invalid coffee type."""
        with pytest.raises(TypeError) as excinfo:
            Customer.most_aficionado("Not a Coffee")
        assert "Input must be a Coffee instance." in str(excinfo.value)