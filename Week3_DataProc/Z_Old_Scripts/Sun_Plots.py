#!/usr/bin/env python
execfile('Sun_Script.py')
SUN_PLOT = True

N_Points = len(Voltage)
dt = Time[1] - Time[0]

# if SUN_PLOT:
Sun_PhysG = plt.figure()
plt.plot(Time,Voltage)

def PlotPower(Signal,dt):
    N = len(Signal)
    Sig_Freqs = fft(Signal)
    FreqAx = fftshift(fftfreq(N,dt))
    Sig_Power = np.abs(fftshift(Sig_Freqs))
    Sig_PowerG = plt.figure()
    plt.plot(FreqAx,Sig_Power)
    
    return Sig_Freqs, Sig_PowerG, FreqAx, Sig_Power
    
VFour,Sun_FourG,FreqAx,VPower = PlotPower(Voltage,dt)

    
Time_Diffs = [Time[I+1]-Time[I] for I in range(len(Time)-1)]
Time_DiffsG = plt.figure()
plt.plot(Time_Diffs)
plt.show()

dt = Time[1] - Time[0]

print dt
