from item import Item

Item.instanciateFromCsv()

print(Item.all[1].price)
Item.all[1].applyIncrement(2)
print(Item.all[1].price)