import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):

    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    discount = 1 / (1 + r) ** t

    cashflows = np.full(n, c)
    cashflows[-1] += face

    price = np.sum(cashflows * discount)
    duration = np.sum(t * cashflows * discount) / price

    return duration / ppy
