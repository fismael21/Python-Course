#Simple Function
def greet():
  print("Hello, Fernando")
  print("How do you do?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Fernando' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")

greet_with_name("Fernando Ismael")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Fernando Canul", "Merida")

#vs.

greet_with("Merida", "Fernando Canul")

#Calling greet_with() with Keyword Arguments
greet_with(location="Merida", name="Fernando Canul")
