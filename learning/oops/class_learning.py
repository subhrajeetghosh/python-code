#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh

class Item:
    def __init__(self):
        print("I am created!")

    @staticmethod
    def calc_total_price(price, quantity):
        return price * quantity


item1 = Item()
item1.type = "Mobile"
item1.price = 2410
item1.count = 5
print(item1.calc_total_price(item1.price, item1.count))

item2 = Item()
item2.type = "Laptop"
item2.price = 35235
item2.count = 2
print(item2.calc_total_price(item2.price, item2.count))

print("\n")


class ItemConst:
    def __init__(self, product: str, price: int, quantity=0):
        assert price > 0, f"Price {price} is not valid!"
        assert quantity > 0, f"Quantity {quantity} is not valid!"
        assert len(product) > 0, "write a valid Product Name"
        self.product = product
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


product1 = ItemConst("Phone", 100, 9)
print(product1.calculate_total_price())

product2 = ItemConst("Laptop", 24532, 4)
print(product2.calculate_total_price())
