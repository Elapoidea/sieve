import matplotlib.pyplot as plt
from datetime import datetime
from sieve import *

boundaries = []
durations = []

for i in range(int(argv[1]) - 2):
    start_time = datetime.now()

    #print(start_time)

    generate_primes(i + 3)

    #print(datetime.now())

    boundaries.append(i + 3)
    durations.append((datetime.now() - start_time).microseconds)

    #print(datetime.now() - start_time)

plt.scatter(boundaries, durations, label='aaaaa', color='r')
plt.show()

#print(durations)
