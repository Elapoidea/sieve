from sys import argv
from datetime import datetime
from sieve import sift_primes

bound = int(argv[1])
prime_list = [i + 2 for i in range(bound - 1)]
sieve = sift_primes(prime_list, bound)
time_started = datetime.now()

i = 0

while True:
    i += 1

    prime_list = next(sieve)

    print(i, prime_list[-1])

    if i + 2 >= len(prime_list):
        sieve.close()

        break

print(f'\nfinished in {datetime.now() - time_started}')

with open(f'./primes/primes{bound}.txt', 'w') as f:
    f.write('\n'.join([str(i) for i in prime_list]))
