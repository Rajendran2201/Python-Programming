'''
 Write a Python function to generate all possible combinations of a
 given string

'''

from itertools import permutations

def find_combinations(word):
     '''This function takes a word as an input and prints the permutations of the word'''
     combinations = permutations(word)
     for i in list(combinations):
          print(' '.join(i))


word = 'raj'
find_combinations(word)


'''
OUTPUT : 

r a j
r j a
a r j
a j r
j r a
j a r

'''