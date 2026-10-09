# Daniel Tray
# 9/13/2026
# Homework 1


item_price = float(input("Enter the item price: "))
quantity = int(input("Enter the quantity: "))
SALES_TAX = 0.075
subtotal = item_price * quantity
tax_amount = subtotal * SALES_TAX
total = subtotal + tax_amount
print("Subtotal: $", round(subtotal, 2))
print("Tax amount: $", round(tax_amount, 2))
print("Total: $", round(total, 2))
# number 2
hourly_wage = float(input("Enter hourly wage: "))
hours_worked = float(input("Enter total hours worked: "))
if hours_worked > 40:
    base_pay = hours_worked * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * hourly_wage * 1.5

else:
    base_pay = hourly_wage * hours_worked
    vertime_pay = 0
    total_pay = base_pay + overtime_pay

print("Base pay: $", round(base_pay, 2))
print("Overtime pay: $", round(overtime_pay, 2))
print("Total pay: $", round(total_pay, 2))
# number 3
numeric_grade = float(input("Enter your numeric grade: "))
if numeric_grade >= 90:
    letter_grade = "A"
elif numeric_grade >= 80:
    letter_grade = "B"
elif numeric_grade >= 70:
    letter_grade = "C"
elif numeric_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    print("Numeric grade: ", numeric_grade)
    print("Letter grade:", letter_grade)
# number 4
hours_worked = float(input("Enter hours worked: "))
performance_score = float(input("Enter performance score: "))
if hours_worked > 35 and performance_score > 85:
    print("Congratulations! you earned a $100 bonus.")
else:
    hours_needed = 36 - hours_worked
    points_needed = 86 - performance_score
if hours_needed > 0:
    print("You need", hours_needed, "more hours")
if points_needed > 0:
    print("You need", points_needed, "more performance points.")
