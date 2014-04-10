#!/usr/bin/env python
import numpy as np
import pyfits

# Get each column of the data. This takes a while (about 15 seconds or so) the first time you do it.
# Once you have the npy files, they should load pretty darn quick.
def Get_Fits_Data(Fits_Data,Col):
    n = len(Fits_Data)
    Data = range(n)
    for I in range(n):
        Pnt = Fits_Data[I]
        Pnt = Pnt[Col]
        Data[I] = Pnt
    return np.array(Data)
    
# File_Name is a string, so for example 'sun-2013-03-19.fits'
# Make sure you are in the same directory as the fits file 
# when running this. You can add something like 
# os.chdir('File_Directory') to the script to make it do that.
def Fits_to_Npy(File_Name):
    with pyfits.open(File_Name) as Fits_Data:
        Data_Numbers = Fits_Data[1].data
        Data_Head = Fits_Data[1].header
        
    Tracking = Get_Fits_Data(Data_Numbers,0)
    Time = Get_Fits_Data(Data_Numbers,1)
    Voltage = Get_Fits_Data(Data_Numbers,2)
    LST = Get_Fits_Data(Data_Numbers,3)
    JulianDate = Get_Fits_Data(Data_Numbers,4)
    RA = Get_Fits_Data(Data_Numbers,5)
    DEC = Get_Fits_Data(Data_Numbers,6)
    
    # Saves the data as .npy files.
    np.save('Tracking',Tracking)
    np.save('Time',Time)
    np.save('Voltage',Voltage)
    np.save('LST',LST)
    np.save('JulianDate',JulianDate)
    np.save('RA',RA)
    np.save('DEC',DEC)

# Call it like:
Fits_to_Npy('Sun_Data.fits')

# To load the files, write:
Sun_Voltage = np.load('Voltage.npy')
print Sun_Voltage
