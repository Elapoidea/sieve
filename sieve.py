# prime sifting function
# takes an input of a list of numbers. these are the numbers that will be sifted
def sift_primes(primes: list):
    # the divisor of the list of numbers
    divisor = 2

    # can keep going infinitely. the break case is elsewhere
    while True:
        # variable for the new primes
        new_primes = []

        # generate the new list of primes
        for i in primes:
            if i % divisor != 0 or i == divisor:
                new_primes.append(i)

        # set the currently list of primes as the newly generated primes
        primes = [i for i in new_primes]

        # change the divisor to the next number
        divisor = primes[primes.index(divisor) + 1]

        # it's best that this function is a generator function so we can see how
        # it changes step by step
        yield primes
