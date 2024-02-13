Welcome to the coffee shop!

# Declare variables
numberOfCoffeesPurchased = 0
numberOfMuffinsPurchased = 0
numberOfCroissantsPurchased = 0
numberOfCakeSlicesPurchased = 0
priceOfCoffee = 5.0
priceOfMuffin = 4.0
priceOfCroissant = 4.0
priceOfCakeSlice = 6.0
taxRate = .06

# Get input from the customer
numberOfCoffeesPurchased = int(input("please enter the number of coffees bought: "))
numberOfMuffinsPurchased = int(input("please enter the number of muffins bought: "))
numberOfCroissantsPurchased = int(input("please enter the number of croissants bought: "))
numberOfCakeSlicesPurchased = int(input("please enter the number of cake slices bought: "))

# Calculate the total cost of products
total_Coffee_Cost = numberOfCoffeesPurchased * priceOfCoffee
total_Muffin_Cost = numberOfMuffinsPurchased * priceOfMuffin
total_Croissant_Cost = numberOfCroissantsPurchased * priceOfCroissant
total_Cake_Slice_Cost = numberOfCakeSlicesPurchased * priceOfCakeSlice

# Calculate the subtotal
subTotal = numberOfCoffeesPurchased * priceOfCoffee + numberOfMuffinsPurchased * priceOfMuffin + numberOfCroissantsPurchased * priceOfCroissant + numberOfCakeSlicesPurchased * priceOfCakeSlice

# Calculate the tax
taxCost = subTotal * taxRate

# Calculate the total cost
totalCost = subTotal + taxCost

# Display the receipt to the customer
print("------ Receipt ------")
print(f"{numberOfCoffeesPurchased} coffees at $5 each: ${total_Coffee_Cost}")
print(f"{numberOfMuffinsPurchased} muffins at $4 each: ${total_Muffin_Cost}")
print(f"{numberOfCroissantsPurchased} croissants at $4 each: ${total_Croissant_Cost}")
print(f"{numberOfCakeSlicesPurchased} cake slices at $6 each: ${total_Cake_Slice_Cost}")
print(f"Subtotal: ${subTotal}") 
print(f"Tax: ${taxCost}")
print('-----')
print(f"Total Cost: ${totalCost}")
print("------         ------")
print("Please come again!")
