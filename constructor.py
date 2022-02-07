class SuperMarket:
    def __init__(self, name, price, discount):
        self.name= name
        self.price = price
        self.discount= discount
product1 = SuperMarket('Soap',20,0.04)
product2 = SuperMarket('Shampoo',10,0.04)
print(product2.price)
