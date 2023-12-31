import csv


class Item:
    # assign global variable to class, this are called --> Class attribute
    payRate = 0.8
    all = []
   
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # received arguments validators
        assert price > 0, "price is less than zero"
        assert quantity > 0, "quantity is less than zero"

        #Instance attribute
        #^^^^^^^^^^^^^^^^^^
        # assign argument to self, this are called --> Instance attribute
        self.__name = name                                            
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)#append initialized item to [all] list

    
    @property
    # Property decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value 
    
    @property
    def price(self):
        return self.__price

    # Instance method a method that applies to class instance
    def applyDiscount(self):
        self.__price = self.__price * self.payRate
        return self.__price 

    # Instance method a method that applies to class instance
    def applyIncrement(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
        return self.__price 



    @price.setter
    def price(self, value):
        if value < 0:
            return "error"
        else:
            self.__price = value
    
    

    #@classmethod
    #^^^^^^^^^^^
    #used to create instancies of objs from data stucture, all with the __init__ method proprieties
    #like from csv, json or other data stucture file
    @classmethod
    def instanciateFromCsv(cls):#pass class cls reference as first argv
        with open("PythonBasicTheory\OOP\items.csv", "r") as f:
            reader = csv.DictReader(f)
            items =list(reader)
            
        # loop through list items and instantiate the objs

        for item in items:
            newItem = dict()

            for k, v in item.items():
                newItem[k.strip()] = v.strip()

            Item(   
                name=newItem["name"],
                price=float(newItem["price"]),
                quantity=int(newItem["quantity"])
            )
        
    # Static methods
    #^^^^^^^^^^^^^^^
    #used to apply some tipe of logic that can be different per instance
    @staticmethod 
    def isInt(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    


    # methods that return something when obj is called
    # def __str__(self) -> str:
    #     return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __repr__(self) -> str: # same as __str__ method represent info when instance obj is argument of print func 
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"#best practice is to represent the obj same way we create instance of the class, 
                                                                    #so we can copy from cmd and change argument only to instantiate a different obj