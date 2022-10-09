# Other function (more details in the future)
def add(*number):
  total = 0
  for num in number:
    total += num
  return total

n = add(1, 2, 3, 4, 5)

print(f"The number is {n}.")