import matplotlib.pyplot as plt
from datetime import datetime
from sieve import *

boundaries = []
durations = []

test_time = datetime.now()

for i in possible_primes(int(argv[1]) - 2):
    duration_mean = 0

    for j in range(10):
        start_time = datetime.now()

        generate_primes(i + 3)

        duration_mean += (datetime.now() - start_time).microseconds


    boundaries.append(i + 3)
    durations.append(duration_mean/10)

    #print(len(durations), len(possible_primes(int(argv[1]) - 2)))


print(datetime.now() - test_time)

plt.scatter(boundaries, durations, label='aaaaa', color='r')
plt.show()

#print(durations)
