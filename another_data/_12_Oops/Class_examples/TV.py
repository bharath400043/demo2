class Telivision:
    display = "4k LED Display"

    def __init__(self, brand, size, price = 50000):
        self.brand = brand
        self.size = size
        self.price = price

    @classmethod
    def type_of_display(cls):
        print("Display type: ", cls.display)

    def get_tv_details(self):
        print("TV Details: ", self.brand, self.size, self.price, Telivision.display)

Telivision.type_of_display()
samsung = Telivision("Samsung", "30x20")
samsung.get_tv_details()