# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowerCaseName1 = name1.lower()
lowerCaseName2 = name2.lower()

combineString = lowerCaseName1 + lowerCaseName2

t = combineString.count("t")
r = combineString.count("r")
u = combineString.count("u")
e = combineString.count("e")

true = t + r + u + e

l = combineString.count("l")
o = combineString.count("o")
v = combineString.count("v")
e = combineString.count("e")

love = l + o + v + e

loveScore = int(str(true) + str(love))
#print(loveScore)

if (loveScore < 10) or (loveScore > 90):
  print(f"Your love score is {loveScore}, you go together like coke and mentos.")
elif (loveScore >=40) and (loveScore <=50):
  print(f"Your score is {loveScore}, you are alright together")
else:
  print(f"Your score is {loveScore}")
