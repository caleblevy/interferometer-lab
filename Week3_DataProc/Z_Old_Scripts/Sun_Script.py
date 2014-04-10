#!/usr/bin/env python
import numpy as np
from numpy.fft import *
import matplotlib.pyplot as plt
import ephem, pyfits
import os, time, sys
# import radiolab

LOAD = False


Berk = ephem.Observer()
Berk.lat = np.radians(37.8732)
Berk.lon = np.radians(-122.2573)
Berk.date = ephem.now() + 12./24

def Get_Fits_Data(Fits_Data,Col):
    n = len(Fits_Data)
    Data = range(n)
    for I in range(n):
        Pnt = Fits_Data[I]
        Pnt = Pnt[Col]
        Data[I] = Pnt
    return np.array(Data)

BaseDir = os.getcwd()

if LOAD:
    sunFit =  pyfits.open('sun_data.fits')
    sun_Data = sunFit[1].data
    sun_Head = sunFit[1].header

    Tracking = Get_Fits_Data(sun_Data,0)
    Time = Get_Fits_Data(sun_Data,1)
    Voltage = Get_Fits_Data(sun_Data,2)
    LST = Get_Fits_Data(sun_Data,3)
    JulianDate = Get_Fits_Data(sun_Data,4)
    RA = Get_Fits_Data(sun_Data,5)
    DEC = Get_Fits_Data(sun_Data,6)

    os.chdir('Sun_Data')
    np.save('sun_Data','sun_Data')
    np.save('sun_Head','sun_Head')

    np.save('Tracking',Tracking)
    np.save('Time',Time)
    np.save('Voltage',Voltage)
    np.save('LST',LST)
    np.save('JulianDate',JulianDate)
    np.save('RA',RA)
    np.save('DEC',DEC)
else:
    os.chdir('Sun_Data')
    sun_Data = np.load('sun_Data.npy')
    sun_Head = np.load('sun_Head.npy')

    Tracking = np.load('Tracking.npy')[0:24300]
    Time = np.load('Time.npy')[0:24300]
    Voltage = np.load('Voltage.npy')[0:24300]
    LST = np.load('LST.npy')[0:24300]
    JulianDate = np.load('JulianDate.npy')[0:24300]
    RA = np.load('RA.npy')[0:24300]
    DEC = np.load('DEC.npy')[0:24300]

os.chdir(BaseDir)
