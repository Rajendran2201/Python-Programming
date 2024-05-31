# find the number of vowels and consonants in a file 

with open('sample.txt', 'r') as f:
  content = f.read()


vowels = "aeiouAEIOU"
vowel_counter, consonant_counter = 0, 0

for letter in content:
  if letter in vowels:
    vowel_counter += 1
  else:
    consonant_counter += 1

with open("vowelsandconsonants.txt", 'w') as f:
  f.write(f"No of vowels: {vowel_counter}")
  f.write(f"\nNo of consonants:  {consonant_counter}")
  

  


