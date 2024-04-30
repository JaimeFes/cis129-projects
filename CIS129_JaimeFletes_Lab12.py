# Module 12 Lab-12
# Jaime Fletes
# 4/29/2024
# creates a class named pet and recalls pets name, type, and age.

# Create class
class Pet:
    def __init__(self, name="", type="", age=0):
        self.name = name
        self.type = type
        self.age = age

    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age

# Create a Pet object
animal = Pet()

# Enter pet information
pet_Name = input("Enter your pet's name: ")
pet_Type = input("Enter your pet's type: ")

while True:
    try:
        pet_Age = int(input("Enter your pet's age: "))
        if pet_Age < 0:
            print("Please enter a positive number: ")
        else:
            break 
    except ValueError:
        print("Please enter a whole number: ")

# Set values for the pet
animal.setName(pet_Name)
animal.setType(pet_Type)
animal.setAge(pet_Age)

# Display the pet's information
print("Your pet's name is", animal.getName())
print("Your pet's type is", animal.getType())
print("Your pet's age is", animal.getAge())
