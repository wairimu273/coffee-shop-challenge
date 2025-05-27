class Order:
    _all = []

    def __init__(self, customer, coffee, price):
        from customer import Customer  # Lazy import
        from coffee import Coffee     # Lazy import
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if not 1.0 <= float(price) <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order._all.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee