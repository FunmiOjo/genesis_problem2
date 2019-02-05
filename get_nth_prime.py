from nth_prime import nth_prime

def get_nth_prime():
  while True:
    try:
      n = int(input('Please enter a positive integer (n) to calculate the nth prime number: '))
      if n < 1:
        raise ValueError
      break
    except ValueError:
      print('That input was not a positive integer.  Please try again.')
  print(nth_prime(n))

get_nth_prime()  