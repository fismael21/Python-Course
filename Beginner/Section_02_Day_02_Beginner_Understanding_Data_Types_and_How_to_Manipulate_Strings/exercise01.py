# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

number = input("Type a two digit number: ")

first_digit = int(number[0])
second_digit = int(number[1])

print(first_digit + second_digit)
