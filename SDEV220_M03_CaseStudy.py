# SDEV220_M03_CaseStudy.py
# Author: Ryan Moore
# Date: 9/9/23
# Purpose: Creates a super class and a class that inherits its values.
# Allows for user input, saves to classes, and then outputs the data.

# Create Vehicle class
class Vehicle():
    vehicleType = ""

# Create Automobile class, inheriting from Vehicle class
class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        self.vehicleType = vehicleType
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Get input from user.
vehicleType = input("Enter the vehicle's type: ")
year = input("Enter the vehicle's year: ")
make = input("Enter the vehicle's make: ")
model = input("Enter the vehicle's model: ")
doors = input("Enter the vehicle's number of doors: ")
roof = input("Enter the vehicle's roof type: ")

# Initialize Automobile object using given data.
auto = Automobile(vehicleType, year, make, model, doors, roof)

# Print data from auto object.
print("Vehicle Type:", auto.vehicleType)
print("Year:", auto.year)
print("Make:", auto.make)
print("Model:", auto.model)
print("Number of Doors:", auto.doors)
print("Roof:", auto.roof)
