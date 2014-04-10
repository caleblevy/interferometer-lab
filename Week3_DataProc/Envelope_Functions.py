def Find_EnvelopeP(Data,width=50):
    Voltage = Data['Voltage']
    N_Bins = len(Voltage)/width
    Inds = []
    VBins = np.array_split(Voltage,N_Bins)
    Offset = 0
    for Ind,Volt in enumerate(VBins):
        Max_Ind = np.argmax(Volt) + Offset
        Inds.append(Max_Ind)
        Offset += len(Volt)
    
    Envelope = {}
    for Item in Data:
        Envelope[Item] = np.zeros(len(Inds))
        for E_Ind,D_Ind in enumerate(Inds):
            Envelope[Item][E_Ind] = Data[Item][D_Ind]
                                    
    return Envelope

def Find_EnvelopeM(Data,width=50):
    # Trick from real analysis: inf(S) = -sup(-S)
    Data['Voltage'] *= -1.0
    EnvelopeM = Find_EnvelopeP(Data,width)
    Data['Voltage'] *= -1.0
    EnvelopeM['Voltage'] *= -1.0
    
    return EnvelopeM
    
def Local_Frequency(Data,Ind):
    lbda = 0.0280967626992 # Save an import, hard-code this in
    By = 10.0 # Meters
    Ra_Null = np.radians(Data['RA'][Ind])
    Dec_Null = np.radians(Data['DEC'][Ind])
    LST_Null = np.radians(Data['LST'][Ind])
    Hs_Null = LST_Null - Ra_Null
    
    f_f = By/lbda*np.cos(Dec_Null)*np.cos(Hs_Null)
    return f_f
    
def Modulation_Eval(N,f_f,R):
    Sum_Vals = np.zeros(2*N+1)
    for n in xrange(-N,N+1):
        n_fac = np.sqrt(1. - ((1.*n)/N)**2)
        c_fac = np.cos(2*np.pi*f_f*R*n/N)
        Sum_Vals[n+N] = n_fac*c_fac
    Mod_Val = np.sum(Sum_Vals)
    return Mod_Val
    
def Modulation_Function(f_f,N_Points=500,R_Min=0.,R_Max=0.04,N_Sum=1000):
    Mod_Vals = np.zeros(N_Points)
    R_Vals = np.linspace(R_Min,R_Max,N_Points)
    for Ind,R in enumerate(R_Vals):
        Mod_Vals[Ind] = Modulation_Eval(N_Sum,f_f,R)
    return R_Vals,Mod_Vals

def Diameter_Function(Data,Ind):
    f_f = Local_Frequency(Data,Ind)
    R_Vals,Amplitude = Modulation_Function(f_f)
    return R_Vals,Amplitude
    