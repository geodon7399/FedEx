#!/usr/bin/env python
"""
Layer images above one another using alpha blending
"""
from __future__ import division
from pylab import *

def func3(x,y):
    return (10- x/20 + x**50 + y**30)*exp(-x**20-y**20)

# make these smaller to increase the resolution
dx, dy = 0.05, 0.05

x = arange(0, 500, dx)
y = arange(0, 500, dy)
X,Y = meshgrid(x, y)

# when layering multiple images, the images need to have the same
# extent.  This does not mean they need to have the same shape, but
# they both need to render to the same coordinate system determined by
# xmin, xmax, ymin, ymax.  Note if you use different interpolations
# for the images their apparent extent could be different due to
# interpolation edge effects


xmin, xmax, ymin, ymax = amin(x), amax(x), amin(y), amax(y)
extent = xmin, xmax, ymin, ymax
fig = plt.figure(frameon=False)

Z1 = array(([1000,1000]*500 + [1000,1000]*500)*500); Z1.shape = 1000,1000  # chessboard
im1 = imshow(Z1, cmap=cm.gray, interpolation='nearest',
             extent=extent)
hold(True)

Z2 = func3(X, Y)

im2 = imshow(Z2, cmap=cm.jet, alpha=.95, interpolation='bilinear',
             extent=extent)
#axis([xmin, xmax, ymin, ymax])

show()