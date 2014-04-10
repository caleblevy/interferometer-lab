#!/usr/bin/env python
import numpy as np
from numpy.fft import *
import numpy.linalg as lin
import matplotlib.pyplot as plt
import ephem,pyfits,pylab
import os,time
import radiolab


#def Median_Filter(Data,width=100)
N = 2**11
t = np.linspace(0.,np.pi*2*(1.-1./N),N)
freqs = np.linspace(0.,24.4,10)
#sig = np.zeros()

def Four_Plot(t,sig):
    N = len(sig)
    Four = fft(sig)
    Power = fftshift(np.abs(Four))
    dt = t[1] - t[0]
    FreqAx = fftshift(fftfreq(N,dt))
    Fig = plt.figure()

    plt.plot(FreqAx,Power)
    return Fig
    
t1 = np.linspace(0.,2*np.pi,N)
t2 = np.linspace(0.,2*np.pi*(1.-1./N),N)
sig1 = np.sin(t1)
sig2 = np.sin(t2)

Four_Plot(t1,sig1)
Four_Plot(t2,sig2)

sig = np.zeros(N)
for f in freqs:
    sig += np.sin(np.pi*2*f*t)

plt.figure()
plt.plot(t,sig)

#print sig

def BoxCar_Mean_Smooth(Data,width=100,Cmp=np.median):
    N = len(Data)    
    Data = np.concatenate([np.zeros(width/2),Data,np.zeros(width/2-1)])
    BoxCar = np.zeros(N)
    for I in range(width/2,N+width/2):
        relavent_slice = Data[I-width/2:I+width/2]
        Norm = Cmp(relavent_slice)
        
        BoxCar[I-width/2] = Data[I] - Norm
#        print I,Data[I],Norm,BoxCar
    return BoxCar
    
el = BoxCar_Mean_Smooth(sig,10)
#for w in xrange(6,101,2):    
#    el = BoxCar_Mean_Smooth(el,w)
#print np.max(sig-el)
plt.plot(t,el)
plt.show()