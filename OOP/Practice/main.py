from Item import Item

# Item.instantiateFromCsv()

# print(Item.all_items)

item1 = Item("Mobile",100,5)

item1.name = "lappy"

#Throws error since name attribute is read-only
print(item1.name)