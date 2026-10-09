# Daniel Tray
# 9/17/26
# Homework 2

# Scenario 1: Gym Membership Discount Calculator

# Base monthly fees
BASIC_FEE = 40
PREMIUM_FEE = 60
ELITE_FEE = 80
AGE_DISCOUNT = 0.20

# Age & Membership level
age = int(input("Enter your age: "))
membership = input("Enter your membership level- Basic, Premium, Elite: ")

# Basic Membership
if membership == "Basic":
    if age < 18 or age >= 65:
        discount_amount = BASIC_FEE * AGE_DISCOUNT
        amount_due = BASIC_FEE - discount_amount
        print("Original fee: ", round(BASIC_FEE, 2))
        print("Discount: ", round(discount_amount, 2))
        print("Amount due: ", round(amount_due, 2))
    else:
        print("Original fee: ", round(BASIC_FEE, 2))
        print("Discount: ", 0)
        print("Amount due: ", round(BASIC_FEE, 2))

# Premium Membership
elif membership == "Premium":
    if age < 18 or age >= 65:
        discount_amount = PREMIUM_FEE * AGE_DISCOUNT
        amount_due = PREMIUM_FEE - discount_amount
        print("Original fee: ", round(PREMIUM_FEE, 2))
        print("Discount: ", round(discount_amount, 2))
        print("Amount due: ", round(amount_due, 2))
    else:
        print("Original fee: ", round(PREMIUM_FEE, 2))
        print("Discount: ", 0)
        print("Amount due: ", round(PREMIUM_FEE, 2))

# Elite Membership
elif membership == "Elite":
    if age < 18 or age >= 65:
        discount_amount = ELITE_FEE * AGE_DISCOUNT
        amount_due = ELITE_FEE - discount_amount
        print("Original fee: ", round(ELITE_FEE, 2))
        print("Discount: ", round(discount_amount, 2))
        print("Amount due: ", round(amount_due, 2))
    else:
        print("Original fee: ", round(ELITE_FEE, 2))
        print("Discount: ", 0)
        print("Amount due: ", round(ELITE_FEE, 2))

# Invalid Membership
else:
    print("Error! Membership entered does not match.")


# Scenario 2: Seasonal Product Stock Alert

import random

# Randomly generate a stock level between 0 and 75
stock = random.randint(0, 75)

# Minimum stock threshold
threshold = int(input("Enter the minimum stock threshold: "))

# Is it the holiday season
holiday = input("Is it the holiday season? (True/False): ")

# Holiday season
if holiday == "True":
    if stock < threshold * 2:
        decision = "restock this item"
    else:
        decision = "Stock level OK"

# Not a holiday season
else:
    if stock < threshold:
        decision = "restock this item"
    else:
        decision = "Stock level OK"

# Print stock level, stock threshold, holiday season, and restock decision
print("Stock level: ", stock)
print("Stock Threshold: ", threshold)
print("Holiday season: ", holiday)
print("Restock decision: ", decision)
