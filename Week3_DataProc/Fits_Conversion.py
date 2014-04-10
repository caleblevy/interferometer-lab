#!/usr/bin/env python
execfile('Import_Packages.py')


## Global parameters; too lazy to check if done
SAVE = False

BaseDir = os.getcwd()
Object = 'Cygnus-a'
Date = '03-25'
Pnt = True

Data_Dir = Object + '_' + Date
File_Name = Object.lower() + '-2014-' + Date

def Get_Fits_Data(Fits_Data,Col):
    n = len(Fits_Data)
    Data = range(n)
    for I in range(n):
        Pnt = Fits_Data[I]
        Pnt = Pnt[Col]
        Data[I] = Pnt
    return np.array(Data)

def Save_Numpy_Data(Data_Dir,File_Name,Pnt):
    os.chdir(Data_Dir)
    with pyfits.open(File_Name + '.fits') as Fits_Data:
        print Fits_Data[1].columns.names
        Data_Numbers = Fits_Data[1].data
        Data_Head = Fits_Data[1].header
    
    print Data_Head
        
    Tracking = Get_Fits_Data(Data_Numbers,0)
    Time = Get_Fits_Data(Data_Numbers,1)
    Voltage = Get_Fits_Data(Data_Numbers,2)
    LST = Get_Fits_Data(Data_Numbers,3)
    JulianDate = Get_Fits_Data(Data_Numbers,4)
    
    
    os.chdir('Raw')
    np.save('Tracking',Tracking)
    np.save('Time',Time)
    np.save('Voltage',Voltage)
    np.save('LST',LST)
    np.save('JulianDate',JulianDate)
    
    if not Pnt:
        RA = Get_Fits_Data(Data_Numbers,5)
        DEC = Get_Fits_Data(Data_Numbers,6)
        np.save('RA',RA)
        np.save('DEC',DEC)
    
    os.chdir('..')
    os.chdir('..')

if SAVE:
    Save_Numpy_Data(Data_Dir,File_Name,Pnt)
    