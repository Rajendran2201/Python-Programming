with open("jerry.txt", 'r') as f:
  content = f.readlines()
  for i in content:
    print(i)