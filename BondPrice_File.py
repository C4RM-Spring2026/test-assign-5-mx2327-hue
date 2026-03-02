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
