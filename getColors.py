# -*- coding: UTF-8 -*-
# Author: Claude Falbriard
# Email:  falbriard@aol.com 
# Date:  April. 10 2015
# NASA Space Apps Contest
# install instructios
# to install the PIL image processing package, run the command: pip instal PIL at command level
# or access the PIL product page at: http://www.pythonware.com/products/pil/ for executables
# also install Python requests package with: pip install Requests
# see documentation at:  http://docs.python-requests.org/en/latest/
from math import cos 
from PIL import Image
from collections import defaultdict
import math
# for image download, use requests
import requests
import sys
import time

def downloadFile(url, directory) :
    localFilename = url.split('/')[-1]
    with open(directory + '/' + localFilename, 'wb') as f:
        start = time.clock()
        r = requests.get(url, stream=True)
        total_length = r.headers.get('content-length')
        print "total_length = " + str(total_length) 
        total_length = int(total_length)
        dl = 0
        if total_length is None: # no content length header
            f.write(r.content)
        else:
            for chunk in r.iter_content(1024):
                dl += len(chunk)
                f.write(chunk)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s] %s bps" % ('=' * done, ' ' * (50-done), dl//(time.clock() - start)))
                print ''
    return (time.clock() - start)
 
def distance_on_unit_sphere(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians       
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    return arc
    
# image source from URL link:  http://visibleearth.nasa.gov/view.php?id=48244  
# fetch the hight resolution image location:  http://eoimages.gsfc.nasa.gov/images/imagerecords/48000/48244/patagonia_amo_2010355_lrg.jpg
url = 'http://eoimages.gsfc.nasa.gov/images/imagerecords/48000/48244/patagonia_amo_2010355_lrg.jpg'
time_elapsed = downloadFile(url, './')
localFilename = url.split('/')[-1]
im = Image.open('./' + localFilename)
#im = Image.open("C:/GISdata/images/patagonia_amo_2010355_lrg.jpg")
# other similar pictures as research reference 
#im = Image.open("C:/GISdata/images/RioPlata_S2002118_lrg.jpg")
#im = Image.open("C:/GISdata/images/Malvinas.OSW_dec62004.jpg")
from collections import defaultdict
light_blue = 0
pixelcount = 0
by_color = defaultdict(int)
for pixel in im.getdata():
    pixelcount += 1	
    by_color[pixel] += 1
    # identify all light blue algae pixels in color range 
    if (pixel >= (91,169,169)) and (pixel <= (92,170,170)):
        light_blue += int(by_color[pixel])  
        #print "found light blue algae adds: " + str(by_color[pixel]) 
        # iteration done
p = 100.0 * light_blue / pixelcount  
print "Results of Color Analysis\n========================="
print "Picture name is:  " + str(im.filename)
print "found light blue algae count: " +  str(light_blue)     
print "number of total pixel is " +  str(pixelcount)
print "mumber of light blue pixel is " +  str(light_blue)
print "percentage is " +  str(round(p,2))
# Calculate distance for Patagonia picture
lllat = -56
lllon = -75.58
urlat = -36.44
urlon = -54.40
# 
ullat = -36
ullon = -75.58
#
lon1 = lllon; lat1 = lllat; lon2 = urlon ; lat2 = urlat
distance1 = distance_on_unit_sphere(lat1, lon1, lat2, lon2) * 6373
print "Distance South-West (KM): " + str(distance1)
#
lon1 = lllon; lat1 = lllat; lon2 = ullon ; lat2 = ullat
distance2 = distance_on_unit_sphere(lat1, lon1, lat2, lon2) * 6373
print "Distance South-Nort (KM): " + str(distance2)
#
lon1 = ullon; lat1 = ullat; lon2 = urlon ; lat2 = urlat
distance3 = distance_on_unit_sphere(lat1, lon1, lat2, lon2) * 6373
print "Distance West-East (KM): " + str(distance3)
# calculate area of triange
#areat = 0.5 * distance1 * distance2
#print "Area of Triangle South-North-West (KM2): " + str(areat)
#areap = areat * 2
areap = distance2 * distance3
print "Area of Picture): " + str(round(areap,3))
# Algae coverage un km2 
algae_km2 = round((areap * p / 100),3)
print "Alagae coverage in light blue-green measured on picture in KM2: " + str(algae_km2)
algae_m2  = round((areap * 1000 * 1000),2)
# chineese space agency told that 1.5 M2 of lagae solution is capable to supply daily oxigen for 1 astronaut
# unit liters
o2_per_m3 = 1 / 1.5 * 550
print "Total of Oxygen produced per cubic meters is: " + str(round(o2_per_m3,2))
# meters sea coverage average depth of algae bloom  
algae_depth = 100 
print "Alagae maximum depth from sea level in meters is: " + str(algae_depth)
# daily volume of oxigen emission to athmosphere 
total_o2_ltrs = algae_m2 * o2_per_m3 * algae_depth
# daily volume of oxigen emission to athmosphere in tons 
total_o2_tons = total_o2_ltrs / 1000 
# daily volume of oxigen emission to athmosphere in kilotons 
total_o2_ktons = total_o2_tons / 1000 
# daily volume of oxigen emission to athmosphere in megatons 
total_o2_mtons = total_o2_ktons / 1000 
# daily volume of oxigen emission to athmosphere in gigatons 
total_o2_gtons = round((total_o2_mtons / 1000),3) 
print "Atlantic Ecosystem - Daily O2 Emission to Athmosphere in GigaTons (Volume Liters): " + str(total_o2_gtons)
# molecular weight of O2 is 32 g per liter 
total_o2_kgmass = total_o2_ltrs * 0.032 
total_o2_tonsmass = total_o2_kgmass / 1000
total_o2_kilotonssmass = total_o2_tonsmass / 1000
total_o2_megatonssmass = total_o2_kilotonssmass / 1000
total_o2_gigatonsmass = round((total_o2_megatonssmass / 1000),3)
print "Atlantic Ecosystem - Daily O2 Emission to Athmosphere in GigaTons (Mass): " + str(total_o2_gigatonsmass)
# Lookup of Earth Fact Sheet - Athmosphere
# http://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
# Total Volume of Oxygen Earth Athmosphere is
total_mass_kg = 5.1 * 10e18 
print "Total mass of Earth atmosphere (kg): "  + str(round(total_mass_kg,2)) 
# oxygen = 21% of athmosphere  
total_oxygen = total_mass_kg * 0.21  
print "Total mass of Earth Oxygen (kg): "  + str(total_oxygen) 
total_o2_gigatonsmass_earth = round((total_oxygen / 1000.0 / 1000.0 / 1000.0 / 1000.0),3)
print "Total mass of Earth Oxygen (giga tons mass): "  + str(total_o2_gigatonsmass_earth) 
# count days to charge all athmosphere with O2 
charge_days = int(total_o2_gigatonsmass_earth / total_o2_gigatonsmass)
print "Total days required to charge Oxygen into athmosphere: " + str(charge_days)
print "Total years required to charge Oxygen into athmosphere: " + str(math.ceil(charge_days/365.0)) 
# all done