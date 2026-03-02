import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    out = np.array(nums, dtype=object)

    fizz = (nums % 3 == 0)
    buzz = (nums % 5 == 0)

    out[fizz & buzz] = "fizzbuzz"
    out[fizz & ~buzz] = "fizz"
    out[buzz & ~fizz] = "buzz"
    return out
