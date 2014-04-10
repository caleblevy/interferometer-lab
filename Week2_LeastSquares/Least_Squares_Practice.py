#!/usr/bin/env python
import numpy as np
from numpy.fft import *
import numpy.linalg as lin
import matplotlib.pyplot as plt
import ephem,pyfits,pylab
import os,time

Y = np.array([142, 168, 211, 251])
X = np.array([np.array([1,1,1,1]),[5,7,9,11],[25,49,81,121]])
N,M = np.shape(X)

XX = np.dot(X,np.transpose(X))
XXI = lin.inv(XX)
XY = np.dot(Y,np.transpose(X))
a = np.dot(XY,XXI)
YBAR = np.dot(a,X)
DELY = Y - YBAR
s_sq = np.sum(np.dot(DELY/(M-N),np.transpose(DELY)))
Sigma = np.sqrt(s_sq*np.diag(XXI))

print 'X=',X
print 'Y=',Y
print 'XX=',XX
print 'XY=',XY
print 'XXI=',XXI
print 'a=',a
print 'YBAR=',YBAR
print 'DELY=',DELY
print 's_sq=',s_sq
print 'Sigma=',Sigma


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

a,Y_Fit,Del_Y,s_sq,Sigma = Least_Squares(X,Y)
print 'a,Y_Fit,Del_Y,s_sq,Sigma=',a,Y_Fit,Del_Y,s_sq,Sigma
    
# diag_elems = np.dot(NbyNmatrix,np.identity(N))