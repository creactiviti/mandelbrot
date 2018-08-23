import matplotlib.pyplot as plt
from numpy import zeros
from numpy import empty
from numpy import linspace

def julia(z,c,maxiter):
  for iterations in range(maxiter):
    z = (z*z) + c
    if abs(z) > 4:
      break;
  return iterations

xvalues = linspace (-2, 2, 1000)
yvalues = linspace (-2, 2, 1000)
c = complex(-0.05,0.65)

xlen = len(xvalues)
ylen = len(yvalues)

atlas = empty((xlen,ylen))

for ix in range(xlen):
  for iy in range(ylen):
    zr = xvalues[ix]
    zi = yvalues[iy]
    z = complex(zr,zi)
    atlas[ix,iy] = julia(z,c,80)

plt.figure(figsize=(10,10))
plt.imshow(atlas.T, interpolation="nearest")
plt.show()

