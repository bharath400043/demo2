class Mobile:
    battery = "5000Mah"
    camera = "48mp"

    def __init__(self,brand, colour , price):
        self.brand = brand
        self.colour = colour
        self.price = price

    @classmethod
    def get(cls):
        pass

    def mobile_details(self):
        print(self.brand, self.colour, self.price)

redmi = Mobile("Note4","black", 10000)
redmi.mobile_details()
