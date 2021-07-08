def print_range(lower_bound = 1, upper_bound = 101):
  numbers = range(lower_bound, upper_bound)
  for number in numbers:
      if ((number % 3)  == 0) and ((number % 5) == 0):
        print("FizzBuzz")
      elif (number % 5) == 0:
        print("Buzz")
      elif (number % 3) == 0:
        print("Fizz")
      else:
        print (number)

print_range(1, 101)
