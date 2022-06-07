# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# You have 12410 days, 1768 weeks, and 408 months left.

number = int(input(""))

days = (90 - number) * 365
months = (90 - number) * 12
weeks = (90 - number) * 52

print(f"You have {days} days, {weeks} weeks, and {months} months left.")