
# checks if number is prime by trial division
def is_prime(num):
  for i in range(2, int(num**(1/2)) + 1):
    if num % i == 0:
      return False
  return True

# counts primes until reaching n primes
def nth_prime(n):
  quantity_primes = 0
  current_num = 2
  while quantity_primes < n:
    if is_prime(current_num):
      quantity_primes += 1
      if quantity_primes == n:
        return current_num
    current_num += 1
  return current_num


