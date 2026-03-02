import numpy as py
def FizzBuzz(start, finish):
  nums = np.arange(start, finish + 1)
  result = np.array(nums, dtype=object)
  fizz_mask = nums % 3 == 0
    buzz_mask = nums % 5 == 0
result[fizz_mask & buzz_mask] = "fizzbuzz"
esult[fizz_mask & ~buzz_mask] = "fizz"
    result[buzz_mask & ~fizz_mask] = "buzz"
return result
