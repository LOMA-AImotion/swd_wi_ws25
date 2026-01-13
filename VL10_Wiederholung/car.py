class Car:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.produced = False
        
    def print_info(self):
        info_str = f"Car Brand: {self.brand}, Type: {self.model}, Colour: {self.colour}"
        print(info_str)
        
    def produce(self):
        self.produced = True
        
class CityCar(Car): 
    def __init__(self, brand, model, colour, co2_emission):
        super().__init__(brand, model, colour)
        self.co2_emission = co2_emission

    def print_info(self):
        info_str = f"Car Brand: {self.brand}, Type: {self.model}, Colour: {self.colour}, Emission: {self.co2_emission}"
        print(info_str)

    def validate_co2_emission(self):
        if self.co2_emission < 150:
            print("Emission valid!")
        else:
            print("Emission not valid")
        
car1 = Car("Audi", "A5", "Black")
car2 = Car("BMW", "3", "Blue")

car3 = CityCar("Smart", "ForTwo", "Red", 123)

car1.produce()
car3.produce()

car3.validate_co2_emission()

car1.print_info()
car2.print_info()
car3.print_info()
