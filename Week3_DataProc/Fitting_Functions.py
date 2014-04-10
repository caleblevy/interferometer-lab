#!/usr/bin/env python
# Assumes modules from Data_Process already loaded; save module loading time

def BoxCar_Smooth(Data,width=100,Cmp=np.median):
    N = len(Data)    
    Data = np.concatenate([np.zeros(width/2),Data,np.zeros(width/2)])
    BoxCar = np.zeros(N)
    for I in range(width/2,N+width/2):
        relavent_slice = Data[I-width/2:I+width/2+1]
        Norm = Cmp(relavent_slice)
        BoxCar[I-width/2] = Data[I] - Norm
    return BoxCar

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

def Array_Print(Array,Name=None):
    print '    '
    print '    '
    if Name:
        print Name,'= '
    
    print '  ['
    for I in Array:
        print '   ',I
    print '  ]'
    
def Basis_Functions(Hs_Vec,Dec,Baseline):
    # Output is a function of hour angle
    lbda = 0.0280967626992 # Save an import, hard-code this in
    Hs_Vec = Hs_Vec*2*np.pi*np.cos(Dec)*Baseline/lbda
    Cos_Vec = np.cos(Hs_Vec)
    Sin_Vec = -1.0*np.sin(Hs_Vec)
    X = np.array([Cos_Vec,Sin_Vec])
    
    return X

def Find_Baseline(Hs_Vec,Dec,Signal,Range=[5.0,15.0,1000]):
    B_s = Range[0]
    B_f = Range[1]
    N_Tries = Range[2]
    Baselines = np.linspace(B_s,B_f,N_Tries)
    
    S_sq = np.zeros(N_Tries)
    
    for I,By in enumerate(Baselines):
        X = Basis_Functions(Hs_Vec,Dec,By)
        # a,Y_Fit,Del_Y,s_sq,Sigma = Least_Squares(X,Signal)
        a,Y_Fit,Del_Y,s_sq,Sigma = Least_Squares(X,Signal)
        S_sq[I] = s_sq    
    
    return Baselines,S_sq
    
def Best_Fit(Hs_Vec,Dec,Signal,Baselines,S_sq):
    Stats = {}
    S_Ind = np.argmin(S_sq)
    S_Min = S_sq[S_Ind]
    B_Min = Baselines[S_Ind]
    
    Min_Point = np.array([B_Min,S_Min]) # Return
    Min_Basis = Basis_Functions(Hs_Vec,Dec,B_Min)
    Stats['a'],Stats['Y_Fit'],Stats['Del_Y'],Stats['s_sq'],Stats['Sigma'] = Least_Squares(Min_Basis,Signal)
    return Min_Point,Stats
    
def Relevant_Stats(Hs,Dec,Signal,Range=[5.0,15.0,1000]):
    Hs_Vec = np.sin(Hs)
    Baselines,S_sq = Find_Baseline(Hs_Vec,Dec,Signal)
    Min_Point,Stats = Best_Fit(Hs_Vec,Dec,Signal,Baselines,S_sq)
    return Baselines,S_sq,Min_Point,Stats
    
def Square_Basis(Time):
    N = len(Time)
    x_0 = np.zeros(N) + 1.
    x_1 = Time
    x_2 = Time**2
    X = [x_0,x_1,x_2]
    return X
    
def Resolved_Fit(Env_P,Env_M):
    Volt_P = Env_P['Voltage']
    Volt_M = Env_M['Voltage']
    
    X_P = Square_Basis(Env_P['Time'])
    X_M = Square_Basis(Env_M['Time'])
    Stats_P = {}
    Stats_M = {}
    
    Stats_P['a'],Stats_P['Y_Fit'],Stats_P['Del_Y'],Stats_P['s_sq'],Stats_P['Sigma'] = Least_Squares(X_P,Volt_P)
    Stats_M['a'],Stats_M['Y_Fit'],Stats_M['Del_Y'],Stats_M['s_sq'],Stats_M['Sigma'] = Least_Squares(X_M,Volt_M)
    
    return Stats_P,Stats_M
    
def Square_Eval(a,Time):
    x_0 = a[0]
    x_1 = a[1]
    x_2 = a[2]
    return x_0 + x_1*Time + x_2*Time**2

def Interpolate_Fit(Env_P,Env_M,Time):
    Stats_P,Stats_M = Resolved_Fit(Env_P,Env_M)
    a_P = Stats_P['a']
    a_M = Stats_M['a']
    Parab_P = Square_Eval(a_P,Time)
    Parab_M = Square_Eval(a_M,Time)
    return Parab_P,Parab_M
    

def Moon_Fit(MoonE):
    Time = MoonE['Time']
    Period = MoonE['Time'][-1]/4
    Sin_Vec = np.sin(2*np.pi*Time/Period)
    Cos_Vec = np.cos(2*np.pi*Time/Period)
    X = np.array([np.ones(len(Time)),Sin_Vec,Cos_Vec])
    Y = MoonE['Voltage']
    Stats = {}
    Stats['a'],Stats['Y_Fit'],Stats['Del_Y'],Stats['s_sq'],Stats['Sigma'] = Least_Squares(X,Y)
    return Stats
    
    
    
    