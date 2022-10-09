# Lists

states_of_america = ["Delaware", "Pennsylvania", "California"]

print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])

print(states_of_america[-1])

states_of_america[0] = "New York"
print(states_of_america)

states_of_america.append("Texas")
print(states_of_america)

states_of_america.extend(["Fernando", "Ismael"])
print(states_of_america)

# Nested Lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][1])