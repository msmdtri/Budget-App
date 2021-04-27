# Create a class "Category"

class Category:

# Constructor

    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount
        self.ledger = []

# Define the following methods in the class: Deposit, Withdraw, Transfer, Check Balance

# Deposit
    
    def deposit(self, amount):
        self.ledger.append(amount)
        self.amount += amount
        return "You have successfully deposited {} dollars in {} category.".format(amount, self.category)

# Budget Balance
    
    def budget_balance(self):
        return "Please carefully view your current balance: {} dollars.".format(self.amount)
        return self.amount

# Check Balance (Check Balance should return a True or False statement. This method checks if the amount is less or greater than self.amount)
    
    def check_balance(self, amount):
        if  self.amount < amount:
            return False
        else:
            return True

# Withdrawal (Withdrawal is considered reversal of deposit)
    
    def withdrawal(self, amount):
        if self.check_balance(amount) == True:
            self.amount -= amount
            self.ledger.append(amount)
            return "You have successfully withdrawn {} dollars in {} category.".format(amount, self.category)
        else:
            return False
    
# Transfer (Transfer between two instantiated categories) using self withdrawal and category deposit
# Check for sufficient funds to allow for transfer
    
    def transfer(self, category, amount):
        if self.check_balance(amount) == True:
            print("The transfer of funds between two categories is initiated.")
        return self.withdrawal(amount) + " " + category.deposit(amount)
        
# Instantiate objects based on different categories (i.e. Food, Clothing, Car Expenses, etc ...) and their amounts. 

food_category = Category("Food", 500)
clothing_category = Category("Clothing", 300)
car_category = Category("Car Expenses", 600)
rent_category = Category("Rent", 550)
utilities_category = Category("Utilities", 200)
education_category = Category("Education", 50)

# Food Category

print(food_category.deposit(250))
print(food_category.budget_balance())
print(food_category.check_balance(5))
print(food_category.withdrawal(25))
print(food_category.transfer(clothing_category,50))

# Clothing Category

print(clothing_category.deposit(150))
print(clothing_category.budget_balance())
print(clothing_category.check_balance(100))
print(clothing_category.withdrawal(15))
print(clothing_category.transfer(car_category,20))

# Car Expenses Category

print(car_category.deposit(500))
print(car_category.budget_balance())
print(car_category.check_balance(50))
print(car_category.withdrawal(250))
print(car_category.transfer(rent_category,10))

# Rent Expenses Category

print(rent_category.deposit(600))
print(rent_category.budget_balance())
print(rent_category.check_balance(150))
print(rent_category.withdrawal(550))
print(rent_category.transfer(utilities_category,100))

# Utilities Expenses Category

print(utilities_category.deposit(250))
print(utilities_category.budget_balance())
print(utilities_category.check_balance(50))
print(utilities_category.withdrawal(150))
print(utilities_category.transfer(education_category,10))

# Education Category

print(education_category.deposit(100))
print(education_category.budget_balance())
print(education_category.check_balance(20))
print(education_category.withdrawal(50))
print(education_category.transfer(food_category,15))
