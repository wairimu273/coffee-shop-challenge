import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def tearDown(self):
        Customer._all.clear()
        Coffee._all.clear()
        Order._all.clear()

    def test_price_validation(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # Too low
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)  # Too high
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "5.0")  # Wrong type
        with self.assertRaises(ValueError):
            Order("not a customer", self.coffee, 5.0)  # Wrong customer type
        with self.assertRaises(ValueError):
            Order(self.customer, "not a coffee", 5.0)  # Wrong coffee type

    def test_properties(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_price_immutability(self):
        order = Order(self.customer, self.coffee, 5.0)
        with self.assertRaises(AttributeError):
            order.price = 6.0  # Should be immutable

if __name__ == "__main__":
    unittest.main()