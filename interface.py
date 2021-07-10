# imports
from sys import argv
from datetime import datetime
from sieve import sift_primes

# the biggest number in the default prime range
bound = int(argv[1])

# base list of primes. this will soon be appended to with numbers adjacent to
# a multiple of 6 within the range of [bound]
prime_list = [2, 3]

# while loop paired with a counting variable
# this is used instead of a for loop because I can't know how many multiple of
# six adjacent numbers there will be
i = 0

while True:
    i += 1

    # if one less than a multiple of six is within [bound], add it to the list
    # otherwise break out of the loop
    if 6 * i - 1 <= bound:
        prime_list.append(6 * i - 1)
    else:
        break

    # same thing as before, but with one more than a multiple of six
    if 6 * i + 1 <= bound:
        prime_list.append(6 * i + 1)
    else:
        break

# bind the sieving function
sieve = sift_primes(prime_list)

# get the time started
# this will be used later to calculate how long it took to generate the primes
time_started = datetime.now()

# while loop paired with a counting variable
# the counting variable, [i], is so I can calculate when to stop the sieve
i = 0

while True:
    i += 1

    # generate the next step in the prime list
    prime_list = next(sieve)

    # print the index, along with the largest number in the current list of primes
    print(i, prime_list[-1])

    # if the next cycle is going to be the end of the calculation -- i.e. it has
    # checked every number in the prime list -- then break the loop and close
    # the function
    if i + 2 >= len(prime_list):
        sieve.close()

        break

# calculate the time taken to generate the primes
calculation_time = datetime.now() - time_started
# after that, insert it into the list of primes
# this is done so the file is saved with the calculation time
prime_list.insert(0, f'* {str(calculation_time)}')

# print the time taken
print(f'\nfinished in {calculation_time}')

# savse the file with [prime_list], which includes all the calculated
# primes, and the time taken to generate those primes
with open(f'./primes/primes{bound}.txt', 'w') as f:
    f.write('\n'.join([str(i) for i in prime_list]))
