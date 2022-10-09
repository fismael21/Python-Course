#{key: value}

programming_dictionary = {
  "Bug": "A bug is an error in a program that prevents the program from running as expected.", 
  "Function": "A function is a piece of code that you can easily call over and over again.",
  "Loop": "A loop is the action of doing something over and over again.",
}

programming_dictionary_2 = {
  1: "A bug is an error in a program that prevents the program from running as expected.", 
  2: "A function is a piece of code that you can easily call over and over again.",
  3: "A loop is the action of doing something over and over again.",
}

#Retrieving items from dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary_2[2])

#Adding new items to  dictionary
programming_dictionary["Repository"] = "A software repository is a storage location for software packages. Often a table of contents is also stored, along with metadata."
print(programming_dictionary["Repository"])

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

#Loop through a dictionary (key)
for key in programming_dictionary:
  print(key)

#Loop through a dictionary (value)
for key in programming_dictionary:
  print(programming_dictionary[key])
