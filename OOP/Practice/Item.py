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
        self.__name = name #double underScore makes the attribute private
        self.price = price
        self.quantity = quantity


        #Actions to execute
        Item.all_items.append(name)


    def calculateTotalPrice(self) -> float:
        return self.price * self.quantity

    def applyDiscount(self):
        self.price = self.price * self.pay_rate

    #To make "name" attribute as read only
    @property
    def name(self):
        return self.__name

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

