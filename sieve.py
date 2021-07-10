from math import log, ceil

def sift_primes(primes: list, bound: int):
    start = 2

    while True:
        new_primes = []

        for i in primes:
            if i % start != 0 or i == start:
                new_primes.append(i)

        primes = [i for i in new_primes]
        start = primes[primes.index(start) + 1]

        yield primes
