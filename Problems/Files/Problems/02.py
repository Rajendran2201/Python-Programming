# Check prime numbers in a file and write them into another file

def check_prime(number):
  number = int(number)
  for i in range(2,number):
    if number % i == 0:
      return False
  return True


with open('numbers.txt', 'r') as f:
  content = f.read()

with open("primes.txt", 'w') as f:
  for number in content:
    is_prime = check_prime(number)
    if is_prime:
      f.write(number)
