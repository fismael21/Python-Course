from os import system
from art import logo

print(logo)

secret_auction = {}

def addData(name, bid):
  secret_auction[name] = bid

flag = True

while(flag):
  name = input("What's your name?: ")
  bid = int(input("How much is your bid?: $"))

  addData(name, bid)
  option = input("Does other user want to bid? Y/N: ");

  if(option == "Y" or option == "y"):
    flag = True
    system("cls")
  elif(option == "N" or option == "n"):
    flag = False
    system("cls")

    highest = 0
    nameHighest = ""

    for key in secret_auction:
      if(secret_auction[key] >= highest):
        highest = secret_auction[key]
        nameHighest = key

  else:
    flag = False

print(f"The winner is {nameHighest}.")

print(secret_auction)
