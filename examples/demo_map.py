from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import string
import matplotlib.cm as cm
   
x = [-105.16, -117.16, -77.00, -114.21, -88.10]
y = [40.02, 32.73, 38.55, 48.25, 17.29]
z=[100, 500, 50, 1000, 400]

m = Basemap(projection='ortho', lon_0=-73,lat_0=38,resolution='l')

x1,y1=m(x,y)

m.drawmapboundary(fill_color='black') # fill to edge
m.drawcountries()
m.fillcontinents(color='white',lake_color='black',zorder=0)


m.scatter(x1,y1,marker="o",cmap=cm.cool,alpha=0.7)
plt.title("Flickr Geotagging Counts with Basemap")
plt.show()