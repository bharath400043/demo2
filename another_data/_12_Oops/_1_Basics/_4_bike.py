class Bike:
    company = "Bajaj"
    def __init__(self, brand, colour, price):
        self.brand = brand
        self.colour = colour
        self.price = price

    @classmethod
    def get_company_name(cls):
        print("Bike Company Name: ", cls.company)

    def get_bike_details(self):
        print(self.brand, self.colour, self.price)

Bike.get_company_name()
pulsar = Bike("Pulsar", "Red", 130000)
pulsar.get_bike_details()
discover = Bike("Discover", "blue", 900000)
discover.get_company_name()
discover.get_bike_details()