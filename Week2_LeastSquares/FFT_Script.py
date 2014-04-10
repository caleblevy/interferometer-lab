#!/usr/bin/env python
import numpy as np
from numpy.fft import *
import matplotlib.pyplot as plt
import ephem,pyfits,pylab
import time,os

n = 100
x_s = -1.
x_f = 1.

x = np.linspace(x_s,x_f,100)
y = x**2

dx = x[1]-x[0]
Freqs = fftfreq(n,dx)
y_Four = fft(y)

Fig = plt.figure()
# plt.plot(x,y)
Trans = np.zeros(n,dtype=complex)
Transx = np.linspace(0,x_f-x_s,n)
for I in xrange(n):
    Trans += y_Four[I]*np.exp(2.*np.pi*1j*Freqs[I]*Transx)/n
    plt.plot(x,np.real(Trans))

Trans = np.real(Trans)

print Trans
print x
print y
# plt.plot(x,fftshift(Trans)/n)
# plt.plot(x,Trans)
pylab.show()
