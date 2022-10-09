student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"

#TODO-1: Create an empty dictionary called student_grades.

#Empty dictionary
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

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
    
# 🚨 Don't change the code below 👇
print(student_grades)