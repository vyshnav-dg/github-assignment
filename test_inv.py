import unittest
from inv import Item, Inventory

class TestInventorySystem(unittest.TestCase):

    def setUp(self):
        self.inv = Inventory()
        self.item1 = Item("Laptop", 10, 50000)
        self.item2 = Item("Mouse", 50, 500)

    def test_add_item(self):
        self.inv.add_item(self.item1)
        self.assertEqual(self.inv.get_item("Laptop"), self.item1)

    def test_add_existing_item_raises(self):
        self.inv.add_item(self.item1)
        with self.assertRaises(ValueError):
            self.inv.add_item(self.item1)

    def test_remove_item(self):
        self.inv.add_item(self.item2)
        self.inv.remove_item("Mouse")
        self.assertIsNone(self.inv.get_item("Mouse"))

    def test_update_quantity(self):
        self.item1.update_quantity(-5)
        self.assertEqual(self.item1.quantity, 5)

    def test_update_price(self):
        self.item2.update_price(600)
        self.assertEqual(self.item2.price, 600)

    def test_total_value(self):
        self.inv.add_item(self.item1)
        self.inv.add_item(self.item2)
        expected = (10 * 50000) + (50 * 500)
        self.assertEqual(self.inv.total_value(), expected)

    def test_negative_quantity_raises(self):
        with self.assertRaises(ValueError):
            Item("Keyboard", -1, 1000)

    def test_insufficient_stock_raises(self):
        with self.assertRaises(ValueError):
            self.item1.update_quantity(-20)

if __name__ == '__main__':
    unittest.main()