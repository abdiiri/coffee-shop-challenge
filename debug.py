from customer import Customer
from coffee import Coffee
from order import Order

if __name__ == '__main__':
    print("Starting debug session...")

    try:
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        coffee3 = Coffee("Cappuccino")
    
        print(f"Created coffee: {coffee1.name}")
        print(f"Created coffee: {coffee2.name}")
        print(f"Created coffee: {coffee3.name}")
    except (TypeError, ValueError) as e:
        print(f"Error creating coffee: {e}")

    print("-" * 20)

    try:
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        print(f"Created customer: {customer1.name}")
        print(f"Created customer: {customer2.name}")
        customer1.name = "Alicia" 
        print(f"Updated customer name: {customer1.name}")
    except (TypeError, ValueError) as e:
        print(f"Error creating/updating customer: {e}")

    print("-" * 20)

    if 'coffee1' in locals() and 'customer1' in locals():
        try:
            order1 = Order(customer1, coffee1, 3.50)
            order2 = customer1.create_order(coffee2, 4.00)
            order3 = Order(customer2, coffee1, 3.75)
            order4 = Order(customer2, coffee2, 4.25)
            order5 = Order(customer1, coffee1, 3.60) 

            print(f"Order 1: {order1.customer.name} ordered {order1.coffee.name} for ${order1.price:.2f}")
            print(f"Order 2: {order2.customer.name} ordered {order2.coffee.name} for ${order2.price:.2f}")
            print(f"Order 3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price:.2f}")

        except (TypeError, ValueError) as e:
            print(f"Error creating order: {e}")

    print("-" * 20)

    if 'customer1' in locals() and 'coffee1' in locals():
        print(f"{customer1.name}'s orders:")
        for o in customer1.orders():
            print(f"  - {o.coffee.name} for ${o.price:.2f}")

        print(f"\n{customer1.name}'s unique coffees ordered:")
        for c in customer1.coffees():
            print(f"  - {c.name}")

        print(f"\nOrders for {coffee1.name}:")
        for o in coffee1.orders():
            print(f"  - By {o.customer.name} for ${o.price:.2f}")

        print(f"\nCustomers who ordered {coffee1.name}:")
        for cust in coffee1.customers():
            print(f"  - {cust.name}")

    print("-" * 20)

    if 'coffee1' in locals() and 'coffee2' in locals():
        print(f"Number of orders for {coffee1.name}: {coffee1.num_orders()}")
        print(f"Average price for {coffee1.name}: ${coffee1.average_price():.2f}") 

        print(f"Number of orders for {coffee2.name}: {coffee2.num_orders()}") 
        print(f"Average price for {coffee2.name}: ${coffee2.average_price():.2f}") 

        if 'coffee3' in locals():
            print(f"Number of orders for {coffee3.name}: {coffee3.num_orders()}") 
            print(f"Average price for {coffee3.name}: ${coffee3.average_price():.2f}") 

    print("-" * 20)

    if 'coffee1' in locals() and 'coffee2' in locals():
        aficionado_coffee1 = Customer.most_aficionado(coffee1)
        if aficionado_coffee1:
            
            print(f"Most aficionado for {coffee1.name}: {aficionado_coffee1.name}") 
        else:
            print(f"No one has ordered {coffee1.name} yet.")

        aficionado_coffee2 = Customer.most_aficionado(coffee2)
        if aficionado_coffee2:
            
            print(f"Most aficionado for {coffee2.name}: {aficionado_coffee2.name}")
        else:
            print(f"No one has ordered {coffee2.name} yet.")

        if 'coffee3' in locals():
            aficionado_coffee3 = Customer.most_aficionado(coffee3)
            if aficionado_coffee3:
                print(f"Most aficionado for {coffee3.name}: {aficionado_coffee3.name}")
            else:
                print(f"No one has ordered {coffee3.name} yet.")

    print("\nDebug session finished.")