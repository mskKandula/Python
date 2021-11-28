from Item import Item

# Item.instantiateFromCsv()

# print(Item.all_items)

item1 = Item("Mobile",100,5)

item1.name = "lappy"

#Doesn't throw any error , since we defined the setter
print(item1.name)