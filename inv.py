class Item:
    def __init__(self, name, quantity, price):
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative")
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock")
        self.quantity += amount

    def update_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price must be non-negative")
        self.price = new_price


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name in self.items:
            raise ValueError("Item already exists")
        self.items[item.name] = item

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError("Item not found")
        del self.items[name]

    def get_item(self, name):
        return self.items.get(name)

    def total_value(self):
        return sum(item.quantity * item.price for item in self.items.values())