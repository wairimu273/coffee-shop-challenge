
from customer import Customer
from coffee import Coffee
from order import Order

if name == "main":

# Create customers and coffees
alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Test name validation and setter
print(f"Customer name: {alice.name}")
alice.name = "Alicia"
print(f"Updated customer name: {alice.name}")

# Test order creation
order1 = alice.create_order(latte, 5.0)
order2 = alice.create_order(espresso, 3.0)
order3 = bob.create_order(latte, 4.0)

# Test relationships
print(f"Alice's orders: {[order.price for order in alice.orders()]}")
print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
print(f"Latte's orders: {[order.price for order in latte.orders()]}")
print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")

# Test aggregates
print(f"Latte num orders: {latte.num_orders()}")
print(f"Latte average price: {latte.average_price()}")

# Test most aficionado
most_aficionado = Customer.most_aficionado(latte)
print(f"Most aficionado for Latte: {most_aficionado.name if most_aficionado else None}")