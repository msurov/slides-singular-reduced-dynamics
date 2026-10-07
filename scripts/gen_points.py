import numpy as np

xmax = 321.52
ymax = 118.07
border = 6
xdiap = [border, xmax - border]
ydiap = [border, ymax - border]
npoints = 5
nsamples = 5


def format_pair(p):
  x, y = p
  x = xdiap[0] + x * (xdiap[1] - xdiap[0])
  y = ydiap[0] + y * (ydiap[1] - ydiap[0])
  x = int(x + 0.5)
  y = int(y + 0.5)
  return f'{x},{y}'

for i in range(nsamples):
  rands = np.random.rand(npoints, 2)
  vals = '; '.join((format_pair(p) for p in rands))
  print(vals)
