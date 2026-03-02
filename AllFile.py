def WhoAmI():
  return('mx2327')
import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    y_period = y / ppy
    coupon = face * couponRate / ppy

    t = np.arange(1, n + 1)
    discount = 1 / (1 + y_period) ** t

    pv_coupons = coupon * discount
    pv_face = face / (1 + y_period) ** n

    price = np.sum(pv_coupons) + pv_face
    return price
import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    C = face * couponRate / ppy
  
    t = np.arange(1, n + 1)
    pv = 1 / (1 + r) ** t
  
    cf = np.full(n, C, dtype=float)
    cf[-1] += face
  
    pvcf = cf * pv
    price = np.sum(pvcf)

    w = pvcf / price
    dur_in_periods = np.sum(t * w)
    return dur_in_periods / ppy

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
