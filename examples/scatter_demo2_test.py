"""
make a scatter plot with varying color and size arguments
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import dType

# load a numpy record array from yahoo csv data with fields date,
# open, close, volume, adj_close from the mpl-data/example directory.
# The record array stores python datetime.date as an object array in
# the date column

#---
datafile = cbook.get_sample_data('goog.npy')
#print datafile
r = np.load(datafile).view(np.recarray)
r = r[-10:] # get the most recent 250 trading days
delta1 = np.diff(r.adj_close)/r.adj_close[:-1]
#print delta1
#print r.volume
#---

##---
#mydescr = np.dtype([('fips', 'S5'), ('state', 'S2'), ('county', 'S20'), ('total', 'int32'), ('__5', 'float32'), ('5_9', 'float32'), ('10_14', 'float32'), ('15_19', 'float32'), ('20_24', 'float32'), ('25_29', 'float32'), ('30_34', 'float32'), ('35_39', 'float32'), ('40_44', 'float32'), ('45_59', 'float32'), ('60_89', 'float32'), ('__90', 'float32'), ('totals', 'int32')])
#datafile = np.genfromtxt('C:/_GEO_DATA/FedExDay/md_travel_data_agg.csv', dtype=mydescr, delimiter=',', names=True)
##print datafile.dtype
#np.save('C:/_GEO_DATA/FedExDay/test.npy', datafile)
##datafile = np.genfromtxt('C:/_GEO_DATA/FedExDay/md_travel_data_agg.csv', dtype=None, delimiter=',', names=True)
#
#r = np.load('C:/_GEO_DATA/FedExDay/test.npy').view(np.recarray)
#r = r[-250:] # get the most recent 250 trading days
#
#delta1 = np.diff(r.__90)/r.__90[:-1]
#print delta1
##---


print 0.003*r.open[:-2]
# size in points ^2
print r.volume
volume = (10*r.volume[:-2]/r.volume[0])**2
#print r.open[:-2]
close = 0.003*r.close[:-2]/0.003*r.open[:-2]

print delta1[:-1]
print delta1[1:]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.75)

#ticks = arange(-0.06, 0.061, 0.02)
#xticks(ticks)
#yticks(ticks)

ax.set_xlabel(r'Age', fontsize=20)
ax.set_ylabel(r'Travel Time', fontsize=20)
ax.set_title('Travel Time with Age')
ax.grid(True)

plt.show()



