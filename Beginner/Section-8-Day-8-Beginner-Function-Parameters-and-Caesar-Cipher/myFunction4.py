#You need to write a function that checks whether if the number passed into it is a prime number or not.

#Write your code below this line ๐

def prime_checker(number):
  if((number % 2) == 0):
    print(f"The number {number} is not prime number.")
  else:
    print(f"The number {number} is a prime numer.")

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
