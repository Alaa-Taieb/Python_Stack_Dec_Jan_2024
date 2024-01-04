# Class definition:
class Car:
    # Lists => Arrays
    # Class Attribute 
    cars = []
    # Constructor
    # 2 instance attributes | color , model , tank_size
    def __init__(self , color , model):
        self.color = color
        self.model = model
        Car.cars.append(self) # push in javascript
    # Attributes
    #   - Instance Attributes
    #   - Class Attributes

    @classmethod
    def number_of_cars(cls):
        print(len(cls.cars))
    # Methods
    #   - Instance Methods
    #   - Class Methods
    #   - Static Methods
    def print_details(self):
        print(f"Color = {self.color} | Model = {self.model}")

    def set_color(self , color):
        self.color = color
    # Instance = Object
    @staticmethod
    def is_valid_model(model):
        # Return true if 'model' is valid
        # Return false if 'model' is not valid
        valid_models = ['Tesla Model S' , 'Tesla Model X']
        return model in valid_models
    
    # Calculates gaz consumption over x distance

print(Car.cars)
Car.number_of_cars()
if Car.is_valid_model("Tesla Model S"):
    car1 = Car("RED" , "Tesla Model S")
if Car.is_valid_model("Tesla Model X"):
    car2 = Car("BLACK" , "Tesla Model X")
if Car.is_valid_model("Tesla Model Y"):
    car3 = Car("YELLOW" , "Tesla Model Y")
if Car.is_valid_model("Tesla Model Z"):
    car4 = Car("PURPLE" , "Tesla Model Z")
Car.number_of_cars()

# for car in Car.cars:
#     car.print_details()


print(Car.is_valid_model("Tesla Model Y"))
# car1.print_details()
# car1.set_color("GREEN")
# car1.print_details()

# car2.print_details()
# car2.set_color("YELLOW")
# car2.print_details()



