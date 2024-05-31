# Write a  Python program to count the number of lines in a text file. 

with open("oggy.txt", 'r') as f:
  content = f.readlines()
  print("No of lines: ",len(content))