student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_of_heights = 0
for height in student_heights:
  sum_of_heights += height

# print(sum_of_heights)

total_of_students = 0
for student in student_heights:
  total_of_students += 1

# print(total_of_students)

avarage_height = round(sum_of_heights / total_of_students)
print(avarage_height)