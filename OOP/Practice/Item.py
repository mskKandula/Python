import csv
class Item:
    pay_rate = 0.8 #class attribute
    all_items =[]

    @classmethod #decorator
    def instantiateFromCsv(cls):  #class method

        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')), #since it reads as type string
                quantity = int(item.get('quantity'))
            )

    def __init__(self,name:str, price:float, quantity=0) -> None:
        
        #Run Validations on received Arguments
        assert price >=0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"

        #Assigning values to self object
        self.name = name
        self.price = price
        self.quantity = quantity


        #Actions to execute
        Item.all_items.append(name)


    def calculateTotalPrice(self) -> float:
        return self.price * self.quantity

    def applyDiscount(self):
        self.price = self.price * self.pay_rate

# item1 = Item("Phone",100,5)

# item2 = Item("Laptop",200,3)

# print(item1.calculateTotalPrice())

# print(item2.calculateTotalPrice())

# print(item1.pay_rate)

# print(item1.__dict__) #To print the whole object as type dict

# item1.applyDiscount()

# print(item1.calculateTotalPrice()) #after discount

# item2.pay_rate = 0.7

# item2.applyDiscount()

# print(item2.calculateTotalPrice())

# Item.instantiateFromCsv()

#Child class Inheriting from Parent Item class 
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0,phones_broken=0) -> None:
        super().__init__(name, price, quantity=quantity)

         #Run Validations on received Arguments
        assert phones_broken >=0, f"Phones Broken {phones_broken} is not greater than or equal to zero!"

        #To initialiaze a new attribute specific to this class
        self.phones_broken = phones_broken

    def validPhonesQuantity(self):
        self.quantity= self.quantity - self.phones_broken

phone1 = Phone("Apple",500000,10,3)

print(phone1.all_items)

print(phone1.calculateTotalPrice())

phone1.validPhonesQuantity()

print(phone1.calculateTotalPrice())