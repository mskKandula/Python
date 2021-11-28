class Item:
    pay_rate = 0.8 #class attribute

    def __init__(self,name:str, price:float, quantity=0) -> None:
        
        #Run Validations on received Arguments
        assert price >=0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"

        #Assigning values to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self) -> float:
        return self.price * self.quantity

    def applyDiscount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone",100,5)

item2 = Item("Laptop",200,3)

print(item1.calculateTotalPrice())

# print(item2.calculateTotalPrice())

print(item1.pay_rate)

print(item1.__dict__) #To print the whole object as type dict

item1.applyDiscount()

print(item1.calculateTotalPrice()) #after discount

item2.pay_rate = 0.7

item2.applyDiscount()

print(item2.calculateTotalPrice())