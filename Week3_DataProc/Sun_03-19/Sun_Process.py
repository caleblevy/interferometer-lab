SLOAD = True
Sun = Data['Sun']
SunP = {}

Clip_Data(Sun,0,24000)
SunP['Raw'] = New_Plot(Sun['Time'],Sun['Voltage'],'yellow')

SunE_P = Find_EnvelopeP(Sun)
SunE_M = Find_EnvelopeM(Sun)

plt.plot(SunE_P['Time'],SunE_P['Voltage'],color='blue')
plt.plot(SunE_M['Time'],SunE_M['Voltage'],color='Red')
plt.gca().set_xlim([0,24000])
Add_Labels(SunP['Raw'],'Raw voltage data for Sun on 03-19', *VT_Labels)
Save_PNG_Plot(SunP['Raw'],'Sun_Envelope')

width = 50
Clip_Data(SunE_P,19000/width,22000/width)
Clip_Data(SunE_M,19000/width,21500/width)

# SunS_P,SunS_M = Resolved_Fit(SunE_P,SunE_M)
Clip_Data(Sun,19000,24000)
plt.gca().set_xlim([19000,24000])
[Parab_P,Parab_M] = Interpolate_Fit(SunE_P,SunE_M,Sun['Time'])
plt.plot(Sun['Time'],Parab_P,Sun['Time'],Parab_M,color='purple')
#plt.plot(SunE_P['Time'],SunS_P['Y_Fit'],SunE_M['Time'],SunS_M['Y_Fit'],color='purple')
Add_Labels(SunP['Raw'],'Null point for sun voltage data', *VT_Labels)
plt.savefig('Sun_Null.pdf')

Sun = Data['Sun']
if not SLOAD:
    Null_Ind = np.where(np.round(Sun['Time']) == 22828)[0][0]
    SunB = {}

    SunB['R'],SunB['Amp'] = Diameter_Function(Sun,Null_Ind)
    SunB['R'] = np.rad2deg(SunB['R'])
    Save_Data(SunB,'Bessel')
else:
    SunB = Load_Data(os.getcwd(),'Bessel')
    Null_Ind = np.where(np.round(Sun['Time']) == 22828)[0][0]
    print Sun['LST'][Null_Ind]

SunP['Diam'] = New_Plot(SunB['R'],SunB['Amp'],'green')
Add_Labels(SunP['Diam'],'Sun Modulation Function at the Null Point',
    'Angular Radius (Degrees)','Amplitude (Arbitrary Units)',Sci=False)
plt.plot(SunB['R'],np.zeros(500),color='black')
plt.plot([0.284],[0.],'yo')
plt.gca().set_xlim([0.,0.6])
plt.savefig('Sun_Diameter.pdf')