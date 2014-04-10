#!/usr/bin/env python
import numpy as np
import numpy.linalg as lin
import numpy.random as ran
import matplotlib.pyplot as plt
import pylab

def Least_Squares(X,Y):
    N,M = np.shape(X)
    XT = np.transpose(X) 
       
    XX = np.dot(X,XT)
    XXI = lin.inv(XX)
    XY = np.dot(Y,XT)

    a = np.dot(XY,XXI)
    Y_Fit = np.dot(a,X)
    Del_Y = Y - Y_Fit
    s_sq = np.sum(np.dot(Del_Y,np.transpose(Del_Y)))/(M-N)
    Sigma = np.sqrt(s_sq*np.diag(XXI))
    
    return a,Y_Fit,Del_Y,s_sq,Sigma

N_Points = 10000
x = np.linspace(0.,3.0,N_Points)
y = 3*x**2 + 2*x + 1.7 #+ 2*(ran.rand(N_Points)-0.5)

f1 = x*0 + 1.
f2 = x
f3 = x**2

X = np.array([f1,f2,f3])
a,Y_Fit,Del_Y,s_sq,Sigma = Least_Squares(X,y)
print 'a=',a
print s_sq
plt.plot(x,y)
plt.plot(x,Y_Fit)
plt.show()