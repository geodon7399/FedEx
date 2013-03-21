"""
make a scatter plot with varying color and size arguments
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab
#import matplotlib.cbook as cbook
#import dType

# load a numpy record array from yahoo csv data with fields date,
# open, close, Total, adj_close from the mpl-data/example directory.
# The record array stores python datetime.date as an object array in
# the date column

##---
#datafile = cbook.get_sample_data('goog.npy')
##print datafile
#r = np.load(datafile).view(np.recarray)
#r = r[-250:] # get the most recent 250 trading days
#delta1 = np.diff(r.adj_close)/r.adj_close[:-1]
##print delta1
#print r.Total
##---

#---
mydescr = np.dtype([('min_range', 'S20'), ('total', 'float32'), ('travel_count', 'float32')])
datafile = np.genfromtxt('C:/_GEO_DATA/FedExDay/stmarys_travel.csv', dtype=mydescr, delimiter=',', names=True)
#print datafile
np.save('C:/_GEO_DATA/FedExDay/stmarys_travel.npy', datafile)
#datafile = np.genfromtxt('C:/_GEO_DATA/FedExDay/md_travel_data_agg.csv', dtype=None, delimiter=',', names=True)

r = np.load('C:/_GEO_DATA/FedExDay/stmarys_travel.npy').view(np.recarray)
#r = r[-250:] # get the most recent 250 trading days

delta1 = np.diff(r.travel_count)/r.travel_count[:-1]
#print delta1
#print r.Total
#---


# size in points ^2
Total = (50*r.Total[:-1]/r.Total[:-1])**2
commuteCat = 0.003*r.travel_count[:-1]/0.003*r.Total[:-1]
#print commuteCat

fig = plt.figure()
ax = fig.add_subplot(111)
print delta1[:-1]
print delta1[1:]
ax.scatter(delta1[:-1], delta1[1:], c='b', s=Total, alpha=0.5)
#ax.bar(11, 11, width='0.8')

#ticks = arange(-0.06, 0.061, 0.02)
#xticks(ticks)
#yticks(ticks)

ax.set_xlabel(r'Age', fontsize=20)
ax.set_ylabel(r'Travel Time', fontsize=20)
ax.set_title('Travel Time with Age')
ax.grid(True)

plt.show()



