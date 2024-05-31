name  = "   My name is Rajendran S   "
name1 = "Raj"
name2 = "Raju"


# Concatenation
print(name1 + name2)
# repetition
print(name1*4)
# Length
print(len(name))
# Membership test
print('r' in name)
# upper and lower
print(name.upper())
print(name.lower())
# strip
print(name.strip())
# replace
print(name.replace('r','$'))
# split
print(name.split(" "))
# join

print(name1.join(name2))
# find
print(name.find('r'))
# startswith, endswith
print(name.startswith("M"))
print(name.endswith("F"))
# capitalize
print(name.capitalize())
# title 
print(name.title())
# count
print(name.count('r'))
# format
print("my name is {}".format(name1))

# isalpha, isdigit, ialnum, isspace