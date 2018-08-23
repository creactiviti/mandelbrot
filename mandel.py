import matplotlib.pyplot as plt
from numpy import zeros
from numpy import empty
from numpy import linspace

def mandel(c,maxiter):
  z = complex(0,0)
  for iterations in range(maxiter):
    z = (z*z) + c
    if abs(z) > 4:
      break;
  return iterations

xvalues = linspace (-0.231, -0.230, 1000)
yvalues = linspace (-0.701, -0.700, 1000)

xlen = len(xvalues)
ylen = len(yvalues)

atlas = empty((xlen,ylen))

for ix in range(xlen):
  for iy in range(ylen):
    cr = xvalues[ix]
    ci = yvalues[iy]
    c = complex(cr,ci)
    atlas[ix,iy] = mandel(c,120)

plt.figure(figsize=(10,10))
plt.imshow(atlas.T, interpolation="nearest")
plt.show()

