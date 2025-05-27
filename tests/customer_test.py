import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.customer2 = Customer("Bob")
        self.coffee = Coffee("Latte")
        self.coffee2 = Coffee("Espresso")

    def tearDown(self):
        Customer._all.clear()
        Coffee._all.clear()
        Order._all.clear()

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  # Empty name
        with self.assertRaises(ValueError):
            Customer("A" * 16)  # Too long
        with self.assertRaises(ValueError):
            Customer(123)  # Wrong type

    def test_name_setter(self):
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")
        with self.assertRaises(ValueError):
            self.customer.name = "A" * 16
        with self.assertRaises(ValueError):
            self.customer.name = 123

    def test_orders_and_coffees(self):
        order1 = self.customer.create_order(self.coffee, 5.0)
        order2 = self.customer.create_order(self.coffee2, 3.0)
        self.assertEqual(self.customer.orders(), [order1, order2])
        self.assertEqual(set(self.customer.coffees()), {self.coffee, self.coffee2})
        self.assertEqual(self.customer2.orders(), [])  # No orders
        self.assertEqual(self.customer2.coffees(), [])  # No coffees

    def test_most_aficionado(self):
        self.customer.create_order(self.coffee, 5.0)
        self.customer.create_order(self.coffee, 3.0)  # Alice: $8.0
        self.customer2.create_order(self.coffee, 4.0)  # Bob: $4.0
        self.assertEqual(Customer.most_aficionado(self.coffee), self.customer)
        self.assertIsNone(Customer.most_aficionado(self.coffee2))  # No orders
        # Test tie case
        self.customer2.create_order(self.coffee, 4.0)  # Bob: $8.0
        most_aficionado = Customer.most_aficionado(self.coffee)
        self.assertIn(most_aficionado, [self.customer, self.customer2])  # Either is valid

if __name__ == "__main__":
    unittest.main()