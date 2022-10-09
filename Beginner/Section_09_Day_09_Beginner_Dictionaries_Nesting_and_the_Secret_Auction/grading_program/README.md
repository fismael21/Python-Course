# Grading Program

## Instructions

You have access to a database of `student_scores` in the format of a dictionary. The **keys** in `student_scores` are the **names** of the students and the **values** are their exam **scores**.

Write a program that **converts their scores to grades**. By the end of your program, you should have a new dictionary called `student_grades` that should contain student **names** for **keys** and their **grades** for **values.** The **final version** of the `student_grades` dictionary will be checked.

**DO NOT** modify lines 1-7 to change the existing `student_scores` dictionary.

**DO NOT** write any print statements.

This is the scoring criteria:

> Scores 91 - 100: Grade = "Outstanding"
>
> Scores 81 - 90: Grade = "Exceeds Expectations"
>
> Scores 71 - 80: Grade = "Acceptable"
>
> Scores 70 or lower: Grade = "Fail"

![Line](https://github.com/fismael21/fismael21/blob/main/img/Line.png)

## Expected Output

```python

'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

```

![Line](https://github.com/fismael21/fismael21/blob/main/img/Line.png)

## Hint

1. Remember that looping through a Dictionary will only give you the **keys** and not the values.

2. If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.

3. At the **end** of your program, the print statement will show the final `student_scores` dictionary, do not change this.

![Line](https://github.com/fismael21/fismael21/blob/main/img/Line.png)

## Solution

```python

#Dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

#Empty dictionary
student_grades = {}

#This function return a string (new string value)
def getCal(value):
  if(value >= 91 and value <= 100):
    return "Outstanding"

  if(value >= 81 and value <= 90):
    return "Exceeds Expectations"

  if(value >= 71 and value <= 80):
    return "Acceptable"

  if(value <= 70):
    return "Fail"

  return 0;

#We copy the keys to the new dictionary, but with new values
for key in student_scores:
  student_grades[key] = getCal(student_scores[key])

#Printing new dictionary
print(student_grades)

```

![Line](https://github.com/fismael21/fismael21/blob/main/img/Line.png)
