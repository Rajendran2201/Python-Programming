with open('sample_numbers.txt', 'r') as f:
  content = f.readlines()

total = 0
numbers = "0123456789"
for i in content:
  number = ""
  for j in i:
    if j in numbers:
      number += j
  total += int(number)

print(total)
