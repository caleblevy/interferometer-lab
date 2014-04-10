#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pylab
import os,time
import ephem

t_f = 3.
N_Points = 1000

T = np.linspace(0,t_f,N_Points) + np.float(ephem.now())
x = np.zeros(N_Points)
y = np.zeros(N_Points)
z = np.zeros(N_Points)

## Global, static variable
Berk = ephem.Observer() # We observe from Berkeley
Sun = ephem.Sun()

Berk_lat = 37.8732
Berk_long = 360.-122.2573

Berk.lat = np.radians(Berk_lat)
Berk.long = np.radians(Berk_long)

for t in T:
    Berk.date = t
    Sun.Compute(Berk)