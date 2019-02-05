from nth_prime import nth_prime

def prime_test():
  result = nth_prime(10000)
  if result == 104729:
    print('Test passed')
  else:
    print('Test failed.  Expected output of {0} but received {1}'.format(104729, result))

prime_test()