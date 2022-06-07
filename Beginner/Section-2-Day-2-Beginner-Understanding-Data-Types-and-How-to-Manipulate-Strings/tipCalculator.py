# If the bill was $150, split between 5 people, with 12% tip.
# Each person should pay (150.00 * 1.12) / 5
# Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!\n")
total_bill = float(input("What was the total bill? $"))

percentage_bill = 1 + (float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100)

people_bill = int(input("How many poeple to split the bill? "))

each_people_pay = round((total_bill * percentage_bill / people_bill), 2)

print(f"Each person should pay: ${each_people_pay}")