from Item import Item

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

# phone1 = Phone("Apple",500000,10,3)

# print(phone1.all_items)

# print(phone1.calculateTotalPrice())

# phone1.validPhonesQuantity()

# print(phone1.calculateTotalPrice())