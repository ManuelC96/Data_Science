import csv


class Item:
    # assign global variable to class, this are called --> Class attribute
    payRate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # received arguments validators
        assert price > 0, "price is less than zero"
        assert quantity > 0, "quantity is less than zero"

        # assign argument to self, this are called --> Instance attribute
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def applyDiscount(self):
        self.price = self.price * self.payRate

    @classmethod
    def instanciateFromCsv(cls):
        with open("items.csv") as f:
            reader = csv.DictReader(f)

    # def __str__(self) -> str:
    #     return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


for item in Item.all:
    print(item)
