# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:

    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def full_name(self):
        return f"The brand is {self.brand} and model is {self.model}."
    

    def get_brand(self):
        return self.brand + " from getter !"
    
    # Polymorphism

    def fuelType(self):
        return "Petrol or Diesel"
    

    @staticmethod
    def general_description():
        return "Cars are means of transport."



my_car = Car("toyota", "corolla")

new_car = Car("tata", "safari")

print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

print(new_car.brand)
print(new_car.model)
print(new_car.full_name())



# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuelType(self):
        return "Electric charge"

Tesla = ElectricCar ("Tesla", "Y", "150kwh")

print(Tesla.brand)
print(Tesla.model)
print(Tesla.battery_size)
print(Tesla.full_name())


# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car1:
    def __init__(self, brand, model):

        # adding __ infront of any attribute makes it private.
        
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return f"The brand is {self.__brand} and model is {self.__model}."
    

    def get_brand(self):
        return self.__brand + " from getter !"
    

        

    @property
    def model (self):
        return self.__model


my_car1 = Car1("toyota", "corolla")

new_car1 = Car1("tata", "safari")

print(my_car1.get_brand())
print(my_car1.model)
print(my_car1.full_name())

print(new_car1.get_brand())
print(new_car1.model)
print(new_car1.full_name())


# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.


print (my_car.fuelType())

print(Tesla.fuelType())


# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

print("Total no. of cars created is : ", Car.total_cars)



# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.


    # Static method is a method that belongs to the class rather than the instance of the class.

print (Car.general_description())


# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

# my_car1.model = "City" # gives error as : AttributeError: property 'model' of 'Car1' object has no setter

print ("my car 1 model is : ", my_car.model)


# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

print (isinstance(Tesla, Car))           # True

print (isinstance(Tesla, ElectricCar))   # True


# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Battery:
    def battery_info(self):
        return "This is battery."

class Engine:
    def engine_info(self):
        return "This is engine."

class ElectricCar2(Battery, Engine):
    pass

byd = ElectricCar2()
print(byd.battery_info())
print(byd.engine_info())