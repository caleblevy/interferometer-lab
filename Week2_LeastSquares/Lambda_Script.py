#!/usr/bin/env python
import numpy as np
from numpy.fft import *
import matplotlib.pyplot as plt
import ephem,pyfits,pylab
import time,os

def Exp_Basis(Freqs):
    Funcs = [lambda x:np.exp(np.pi*2.*1j*I*x) for I in Freqs]
    return Funcs

a = Exp_Basis([1,2.,3,4,5])
print a[1]
print a[1](4)
g = lambda x:np.exp(np.pi*x)
print g(4+1j/4.6)
print a[1](np.arange(5)/7.*1)
print np.arange(5)/7.
