class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, expirationDate=0):

        #call to super function in  order to have fully access to all attribute/methods of parent(super) class
        super().__init__(
            name, 
            price, 
            quantity
            )

        self.expirationDate = expirationDate