#!/usr/bin/env python
execfile('Import_Packages.py')
execfile('Processing_Functions.py')
execfile('Fitting_Functions.py')
execfile('Plotting_Functions.py')
execfile('Envelope_Functions.py')

### Procedural Matters
CAS = False
CRAB = False
CYGNUS = False

SUN = True
MOON = True

Data_Plots = {}
Data = {}

VT_Labels = ('Time (Seconds)','Voltage')
        
### Load all the objects
    
Objects = ['Cas-a','Crab-Nebula','Cygnus-a','Moon','Sun']
Dates = ['03-24','03-26','03-25','03-26','03-19']
Data_Dirs = [None]*5

for I in range(5):
    Data_Dirs[I] = Objects[I]+'_'+Dates[I]   
    Data[Objects[I]] = Load_Data(Data_Dirs[I])
    
    Voltage = Data[ Objects[I] ] ['Voltage']
    Time = Data[ Objects[I] ] ['Time']
    
    Data_Plots[Objects[I]] = New_Plot(Time,Voltage,'green')
    
Base_Dir = os.getcwd()
### Specific Objects

if CAS:
    Cas_Dir = Data_Dirs[0]
    os.chdir(Cas_Dir)
    execfile('Cas_Process.py')
    os.chdir(Base_Dir)
            
if CRAB:
    Crab_Dir = Data_Dirs[1]
    os.chdir(Crab_Dir)
    execfile('Crab_Process.py')
    os.chdir(Base_Dir)
    
if CYGNUS:
    Cygnus_Dir = Data_Dirs[2]
    os.chdir(Cygnus_Dir)
    execfile('Cygnus_Process.py')
    os.chdir(Base_Dir)
    
if SUN:
    Sun_Dir = Data_Dirs[4]
    os.chdir(Sun_Dir)
    execfile('Sun_Process.py')
    os.chdir(Base_Dir)
    
if MOON:
    Moon_Dir = Data_Dirs[3]
    os.chdir(Moon_Dir)
    execfile('Moon_Process.py')
    os.chdir(Base_Dir)
    
    
