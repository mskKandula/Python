class Item:
    def __init__(self,name:str, price:float, quantity=0) -> None:
        
        #Run Validations on received Arguments
        assert price >=0
        assert quantity >=0

        #Assigning values to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self):
        return self.price * self.quantity


item1 = Item("Phone",100,5)

item2 = Item("Laptop",200,3)

print(item1.calculateTotalPrice())

print(item2.calculateTotalPrice())