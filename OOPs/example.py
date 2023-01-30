import csv

class Item:
    pay_rate=0.8 # The pay rate after 20% discount
    all=[]
    def __init__(self,name,price,quantity=0) :
        #run validations to the recieved values
        assert price>=0,f"Price {price} is not greater than 0"
        assert  quantity>=0,f"Quantity {quantity}  is not greater than 0"


        #Assign to self object
        #dynamic attribute defining
        self.name=name
        self.price=price
        self.quantity=quantity

        #aAction to execute
        Item.all.append(self)



    def calculate_total(self):
        return  self.price*self.quantity

    def discount(self):
        self.price=self.price* self.pay_rate

    @classmethod
    def instantaite_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)


        for item in items:
            Item(name=item.get('name'),
            price=float(item.get('price')),
            quantity=int(item.get('quantity')))

    @staticmethod
    def _is_integer(num):
        #we will count out the floats that are 0.0
        #for i.e :5.0,10.0
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False





    def __repr__(self) -> str:
          return f"Item('{self.name}',{self.price},{self.quantity})"


class  Phone(Item):

    pass
phone1=Phone('jscphon',500,5)

phone2=Phone('jscphon2',700,5)


# Item.instantaite_from_csv()
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
# print(Item.all)

# for instance in Item.all:
#     print(instance.name)


# print(item1.calculate_total())
# print(item1.pay_rate)#class attribute can be accessed from instance attribute
# print(Item.pay_rate)
# print(Item.__dict__)#bring all attribute for class level
# print(item1.__dict__)#bring all attribute for instance level
# item1.discount()
# print(item1.price)





