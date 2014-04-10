#!/usr/bin/env python
import numpy as np

def ToCart(AngVec):
    alpha = AngVec[0]
    beta = AngVec[1]
    CartVec = np.zeros(3)
    CartVec[0] = np.cos(beta) * np.cos(alpha)
    CartVec[1] = np.cos(beta) * np.sin(alpha)
    CartVec[2] = np.sin(beta)
    return CartVec

def ToAng(CartVec):
    AngVec = np.zeros(2)
    x,y,z = CartVec
    AngVec[0] = np.arctan2(y,x)
    AngVec[1] = np.arcsin(z)
    return AngVec

def normalize(v):
    norm=np.linalg.norm(v)
    if norm==0: 
       return v
    return v/norm

def TimeMat(LST):
    RAH = np.identity(3)
    RAH[0,0] = np.cos(LST); RAH[0,1] = np.sin(LST)
    RAH[1,0] = np.sin(LST); RAH[1,1] = -1.*np.cos(LST)
    return RAH

def LatMat(lat):
    RLA = np.zeros([3,3])
    RLA[0,0] = -1.*np.sin(lat); RLA[0,1] = 0.; RLA[0,2] = np.cos(lat)
    RLA[1,1] = -1.
    RLA[2,0] = np.cos(lat); RLA[2,1] = 0.; RLA[2,2] = np.sin(lat)
    return RLA

def RD_To_AA_Mat(LST,lat):
    RAH = TimeMat(LST)
    RLA = LatMat(lat)
    RAMat = np.dot(RLA,RAH)
    return RAMat

def RD_To_AA(Vec,LST,lat):
    RAMat = RD_To_AA_Mat(LST,lat)
    CartVec = ToCart(Vec)
    TransVec = np.dot(RAMat,CartVec)
    AngVec = ToAng(TransVec)
    AngVec[0] += 0. if AngVec[0] > 0 else 2*np.pi
    return AngVec

