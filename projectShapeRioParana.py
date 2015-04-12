#!/usr/bin/python
#-*- coding: utf-8 -*-
# Nasa Space Apps 2015
# author:  Claude Falbriard 
# date:    Apr. 10 2015
# project shape file over basemap
# source rivers:  wwf 
from  matplotlib.pyplot import gcf
import matplotlib.pyplot as plt
import matplotlib.cm as mcm
import matplotlib.image as mpimg 
from mpl_toolkits.basemap import Basemap
fig = plt.figure(figsize=(12,12))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
# experimental
ax.patch.set_alpha(0.0)
# Plot Basemap instance for Rio Parana, Countries and States
llcrnrlat = -37.4060
llcrnrlon = -73.6453
urcrnrlat = -15.4688
urcrnrlon = -38.3407
# options for projection
#projection = 'stere'
#projection = 'cyl'
#projection = 'lcc'
map = Basemap(projection='lcc',\
	    llcrnrlat=llcrnrlat,urcrnrlat=urcrnrlat,\
            llcrnrlon=llcrnrlon,urcrnrlon=urcrnrlon,\
            lat_1=20.,lat_2=40.,lon_0=-60.,resolution ='l',area_thresh=1000.)
# Add some more info to the map
map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='#99ffff')
map.fillcontinents(color='#cc9966',lake_color='#99ffff')
map.drawcountries()
map.drawstates()
#add shapefile 
# WWF wetland shape file repository - Level 2
# download, unzip and store under local path: C:\GISdata\wetlands_lv2\ 
# source:  https://www.worldwildlife.org/publications/global-lakes-and-wetlands-database-small-lake-polygons-level-2
map.readshapefile('C:\\GISdata\\wetlands_lv2\\glwd_2', 'rivers',color='b')
# draw a marker point for São Paulo
lon = -23.54
lat = -46.56
label = ' Sao Paulo'
x,y = map(lon, lat)
map.plot(x,y, 'bo', markersize=12)
plt.text(x,y, label) 
#
plt.title("Nasa Space Apps Rio de la Plata - Base Map")
plt.show()
fig.savefig('./images/RioDeLaPlata.png', dpi=200)