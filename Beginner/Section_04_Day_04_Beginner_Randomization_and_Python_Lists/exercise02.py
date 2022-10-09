import random

# str_inp = "Hello, from, AskPython"
# op = str_inp.split(", ")
# print(op)

name_string = input("Give me everybody's name, seperated by a comma. ")
names = name_string.split(", ")

num_items = len(names) - 1
random_choice = random.randint(0, num_items)

# print(type(num_items))

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today.")

#Other solution
person_who_pay = random.choice(names)
print(person_who_pay + " is going to buy the meal today.")