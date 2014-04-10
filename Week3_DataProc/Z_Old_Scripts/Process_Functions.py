#!/usr/bin/env python
execfile('Data_Process.py')

def New_Plot(*args):
    Fig = plt.figure()
    plt.plot(*args)
    return Fig

def Clip_Data(Data,x_s,x_f):
    for I in Data:
        Data[I] = Data[I][x_s:x_f]
        


def Boxcar_Filter_Median(Data,width=100):
    Voltage = Data['Voltage']
    N = len(Voltage)

    Voltage = np.concatenate([np.zeros(width/2),Voltage,np.zeros(width/2)])    
    New_Volt = np.zeros(N)
    
    
    for I in xrange(width/2,N+width/2):
        Median = np.median(Voltage[I:I+width+1])
        New_Volt[I] = Voltage[I+width/2] - Median
    Data['Voltage'] = Voltage[width/2:N+width/2]
    
def Boxcar_Filter_Mean(Data,width=100):
    Voltage = Data['Voltage']
    N = len(Voltage)

    Voltage = np.concatenate([np.zeros(width/2),Voltage,np.zeros(width/2)])    
    
    for I in xrange(width/2,N+width/2):
        Mean = np.mean(Voltage[I:I+width+1])
        Voltage[I+width/2] = Mean
    Data['Voltage'] = Voltage[width/2:N+width/2]

def Add_Data_Four(Data):
    Time = Data['Time']
    Voltage = Data['Voltage']
    dt = Time[1] - Time[0]
    N = len(Voltage)
    
    FreqAx = fftshift(fftfreq(N,dt))
    VFour = fftshift(fft(Voltage))
    VPower = np.abs(VFour)
    Data['VFour'] = VFour
    Data['FreqAx'] = FreqAx
    Data['VPower'] = VPower


def Clip_Four(Data,freq_low,freq_hi=np.inf):
    VFour = Data['VFour']
    FreqAx = Data['FreqAx']
    

    N = len(VFour)
    for I in xrange(N):
        if freq_low <= np.abs(FreqAx[I]) <= freq_hi:
            VFour[I] = 0.
    Data['VFour'] = VFour
    Data['VPower'] = np.abs(VFour)
    
N_Clip = 24000
Clip_Data(Data,0,N_Clip)
New_Plot(Data['Time'],Data['Voltage'])

def BoxCar_Mean_Smooth(Data,width=100,Cmp=np.median):
    N = len(Data)    
    Data = np.concatenate([np.zeros(width/2),Data,np.zeros(width/2-1)])
    BoxCar = np.zeros(N)
    for I in range(width/2,N+width/2):
        relavent_slice = Data[I-width/2:I+width/2]
        Norm = Cmp(relavent_slice)
        BoxCar[I-width/2] = Data[I] - Norm
    return BoxCar

#Boxcar_Filter_Median(Data,6)
#New_Plot(Data['Time'],Data['Voltage'])
#
#Add_Data_Four(Data)
#New_Plot(Data['FreqAx'],Data['VPower'])
#
#Clip_Four(Data,0.05)
#New_Plot(Data['FreqAx'],Data['VPower'])
#
#Data['Voltage'] = np.real(ifft(ifftshift(Data['VFour'])))
#New_Plot(Data['Time'],Data['Voltage'])
#
#Boxcar_Filter_Median(Data,500)
#New_Plot(Data['Time'],Data['Voltage'])
#
#Boxcar_Filter_Mean(Data,6)
#New_Plot(Data['Time'],Data['Voltage'])
# 
# 
# 
plt.show()
        

