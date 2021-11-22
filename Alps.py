# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:00:46 2021
Libraries needed: GEOS, Shapely, pyshp, proj, pyproj, cartopy

to install them all at once just type:
   !conda install -c conda-forge cartopy --y


@author: Lorenzo
"""
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import pylab as pl
import shapefile
import geopandas as gpd

#ccrs.PlateCarree()
from matplotlib import rc
import matplotlib.pyplot as plt

rc('text', usetex=True)
rc('font', family='serif')

fig = plt.figure()


#projection and area displayed
central_lon, central_lat = 10, 45
ax = fig.add_subplot(1,1,1,projection=ccrs.Orthographic(central_lon, central_lat))
ax.set_extent([4, 17, 42.5, 48.5])
ax.gridlines(linewidth=0.3,color='#DDDDDD')



ax.add_feature(cfeature.OCEAN.with_scale('10m'))
ax.add_feature(cfeature.COASTLINE.with_scale('10m'), linewidth=0.5)
ax.add_feature(cfeature.BORDERS.with_scale('10m'), linestyle='--', linewidth=0.4)
ax.add_feature(cfeature.LAKES.with_scale('10m'), alpha=0.5)
ax.add_feature(cfeature.RIVERS.with_scale('10m'), linewidth=0.4)
#rivers_10m = cfeature.NaturalEarthFeature('physical','rivers_lake_centerlines','10m')
#ax.add_feature(rivers_10m, facecolor='None')

# sf = shapefile.Reader('ne_10m_rivers_europe.shp')
# for i in np.arange(len(sf.shapes())):

#     points = sf.shape(i).points
#     lons = np.zeros((len(points),1))
#     lats = np.zeros((len(points),1))
#     for ip in range(len(points)):
#         lons[ip] = points[ip][0]
#         lats[ip] = points[ip][1]


#     ax.scatter(lons, lats, marker='.',
#                             color='#9badd1', transform=ccrs.PlateCarree())

#gdf = gpd.read_file('ne_10m_rivers_europe.shp')
#print(gdf.shape)
#print(gdf.head())


#canyons location

lat, lon = pl.loadtxt('ITALY.txt', unpack=True)


ax.scatter(lon,lat, transform=ccrs.PlateCarree(),marker='.', color='#b91414', s=1)




plt.savefig('Alps.pdf')
plt.show()