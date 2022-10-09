# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

smallPrice = 15
mediumPrice = 20
largePrice = 25

#Write your code below this line 👇

#SMALL PIZZA---------------------------------------------------------
if size == "S":
  if add_pepperoni == "Y":
    #Pizza + pepperoni + extra cheese
    if extra_cheese == "Y":
      smallPrice = smallPrice + 2 + 1
      print(f"Your final bill is: ${smallPrice}")
      #Pizza + pepperoni
    elif extra_cheese == "N":
      smallPrice += 2
      print(f"Your final bill is: ${smallPrice}")
  #Pizza + extra cheese
  elif add_pepperoni == "N":
    if extra_cheese == "Y":
      smallPrice = smallPrice + 1
      print(f"Your final bill is: ${smallPrice}")
      #Just the price for small pizza
    elif extra_cheese == "N":
      print(f"Your final bill is: ${smallPrice}")
#MEDIUM PIZZA--------------------------------------------------------
elif size == "M":
  if add_pepperoni == "Y":
    #Pizza + pepperoni + extra cheese
    if extra_cheese == "Y":
      mediumPrice = mediumPrice + 3 + 1
      print(f"Your final bill is: ${mediumPrice}")
    #Pizza + pepperoni
    elif extra_cheese == "N":
      mediumPrice += 3
      print(f"Your final bill is: ${mediumPrice}")
  #Pizza + extra cheese
  elif add_pepperoni == "N":
    if extra_cheese == "Y":
      smallPrice = mediumPrice + 1
      print(f"Your final bill is: ${mediumPrice}")
      #Just the price for medium pizza
    elif extra_cheese == "N":
      print(f"Your final bill is: ${mediumPrice}")
#LARGE PIZZA---------------------------------------------------------
elif size == "L":
  if add_pepperoni == "Y":
    #Pizza + pepperoni + extra cheese
    if extra_cheese == "Y":
      largePrice = largePrice + 3 + 1
      print(f"Your final bill is: ${largePrice}")
    #Pizza + pepperoni
    elif extra_cheese == "N":
      largePrice += 3
      print(f"Your final bill is: ${largePrice}")
  #Pizza + extra cheese
  elif add_pepperoni == "N":
    if extra_cheese == "Y":
      smallPrice = largePrice + 1
      print(f"Your final bill is: ${largePrice}")
      #Just the price for medium pizza
    elif extra_cheese == "N":
      print(f"Your final bill is: ${largePrice}")
else: 
  print("Sorry, you must input S, M, or L.")