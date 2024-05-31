with open("jerry.txt", 'r') as f:
  f.seek(4)
  content = f.read()
  print(content)