"""
make a scatter plot with varying color and size arguments
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

#define data types
mydescr = np.dtype([('FIPS', 'S5'), ('STATE', 'S2'), ('COUNTY', 'S20'), ('Total', 'int32'), ('m_5', 'float32'), ('m_5_9', 'float32'), ('m_10_14', 'float32'), ('m_15_19', 'float32'), ('m_20_24', 'float32'), ('m_25_29', 'float32'), ('m_30_34', 'float32'), ('m_35_39', 'float32'), ('m_40_44', 'float32'), ('m_45_59', 'float32'), ('m_60_89', 'float32'), ('m_90', 'float32'), ('totals', 'int32')])

#read csv into numpy
datafile = np.genfromtxt('C:/_GEO_DATA/FedExDay/md_travel_data_agg.csv', dtype=mydescr, delimiter=',', names=True)
print datafile

#save csv into binary
np.save('C:/_GEO_DATA/FedExDay/md_travel_data_agg.npy', datafile)

#read array of records into memory
r = np.load('C:/_GEO_DATA/FedExDay/md_travel_data_agg.npy').view(np.recarray)

delta1 = np.diff(r.m_90)/r.m_90[:-1]

Total = (20*r.Total[:-1]/r.Total[:-1])**2
commuteCat = 0.003*r.m_90[:-1]/0.003*r.Total[:-1]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(delta1[:-1], delta1[1:], c='b', s=Total, alpha=0.50)

#ax.set_xlabel(r'Age', fontsize=20)
#ax.set_ylabel(r'Travel Time', fontsize=20)
ax.set_title('Travel by MD Counties > 90 min')
ax.grid(True)

plt.show()
