import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.customer2 = Customer("Bob")
        self.coffee = Coffee("Latte")

    def tearDown(self):
        Customer._all.clear()
        Coffee._all.clear()
        Order._all.clear()

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("Ab")  # Too short
        with self.assertRaises(ValueError):
            Coffee(123)  # Wrong type

    def test_name_immutability(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Mocha"  # Should be immutable

    def test_orders_and_customers(self):
        order1 = Order(self.customer, self.coffee, 5.0)
        order2 = Order(self.customer2, self.coffee, 7.0)
        self.assertEqual(self.coffee.orders(), [order1, order2])
        self.assertEqual(set(self.coffee.customers()), {self.customer, self.customer2})
        new_coffee = Coffee("Espresso")
        self.assertEqual(new_coffee.orders(), [])  # No orders
        self.assertEqual(new_coffee.customers(), [])  # No customers

    def test_num_orders_and_average_price(self):
        Order(self.customer, self.coffee, 5.0)
        Order(self.customer2, self.coffee, 7.0)
        self.assertEqual(self.coffee.num_orders(), 2)
        self.assertEqual(self.coffee.average_price(), 6.0)
        new_coffee = Coffee("Espresso")
        self.assertEqual(new_coffee.num_orders(), 0)
        self.assertEqual(new_coffee.average_price(), 0)

if __name__ == "__main__":
    unittest.main()