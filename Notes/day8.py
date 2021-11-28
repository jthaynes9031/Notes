#Functions and Inputs and parameters
def greet(name, location):
    print(f"Hello {name} {location}")
    print("HI")

greet("jon", "winston")

#Functions can take parameters
def prime_checker(number):
  isPrime = True
  for i in range(2, number):
    if number % i == 0:
      isPrime = False
  if isPrime:
    print("is prime number")
  else:
    print("not prime")
n = int(input("Check this number: "))
prime_checker(number=n)