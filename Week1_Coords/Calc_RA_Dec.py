#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pylab
import os,time
import ephem

# def LST_to_Rad(LST):
#     return np.pi*2.*LST/24.

execfile('coordinates.py')
## Global, static variable
Berk = ephem.Observer() # We observe from Berkeley
Sun = ephem.Sun()

Berk_lat = 37.8732
Berk_long = 360.-122.2573

Berk.lat = np.radians(Berk_lat)
Berk.long = np.radians(Berk_long)
Berk.date = ephem.now() # For timezone discrepency

Sun.compute(Berk)
LST = Berk.sidereal_time()
# print np.float(LST)
# LST = LST_to_Rad(LST)
# print LST

Sun_Co = [np.float(Sun.ra),np.float(Sun.dec)]
Sun_Tel = RD_To_AA(Sun_Co,LST,Berk.lat)
print Sun_Tel
print float(Sun.az)
print float(Sun.alt)
