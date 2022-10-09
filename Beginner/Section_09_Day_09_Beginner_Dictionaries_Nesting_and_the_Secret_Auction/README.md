# Dictionaries, Nesting, and the Secret Auction

## Dictionaries in Python

### What is a dictionary in Python?

> [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.

![Line](https://github.com/fismael21/fismael21/blob/main/img/Line.png)

## Example of Dictionaries

```python

#{key: value}

#key (string)
programming_dictionary = {
  "Bug": "A bug is an error in a program that prevents the program from running as expected.",
  "Function": "A function is a piece of code that you can easily call over and over again.",
  "Loop": "A loop is the action of doing something over and over again.",
}

#key (integer)
programming_dictionary_2 = {
  1: "A bug is an error in a program that prevents the program from running as expected.",
  2: "A function is a piece of code that you can easily call over and over again.",
  3: "A loop is the action of doing something over and over again.",
}

#Retrieving items from dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary_2[2])

```

![Line](https://github.com/fismael21/fismael21/blob/main/img/Line.png)

## Output

```python

A bug is an error in a program that prevents the program from running as expected.
A function is a piece of code that you can easily call over and over again.

```

![Line](https://github.com/fismael21/fismael21/blob/main/img/Line.png)

### Code Example

[Grading Program](https://github.com/fismael21/Python-Course/tree/master/Beginner/Section_09_Day_09_Beginner_Dictionaries_Nesting_and_the_Secret_Auction/grading_program)

![Line](https://github.com/fismael21/fismael21/blob/main/img/Line.png)
