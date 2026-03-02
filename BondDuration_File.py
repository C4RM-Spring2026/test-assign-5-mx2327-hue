import numpy as np
def getBondDuration(y, face, couponRate, m, ppy=1):
  n = m * ppy
  r = y / ppy
  C = face * couponRate / ppy
  t = np.arange(1, n + 1)
  pv = 1 / (1 + r) ** t
  cf = np.full(n, C, dtype=float)
  cf[-1]=C+face
pvcf = cf * pv
price = np.sum(pvcf)
w = pvcf / price
dur_in_periods = np.sum(t * w)
dur_in_years = dur_in_periods / ppy
return dur_in_years
