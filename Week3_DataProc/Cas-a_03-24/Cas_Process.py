Cas = Data['Cas-a']
CasP = {}

# Raw Data
CasP['Raw'] = Data_Plots['Cas-a']
Add_Labels(CasP['Raw'], 'Raw data for Cas-a on 03-24', *VT_Labels)
plt.gca().set_xlim([0,len(Cas['Voltage'])])

# Smooth Data
Cas['Smooth'] = Cas['Voltage']
Cas['Smooth'] = BoxCar_Smooth(Cas['Voltage'])
Save_Data(Cas,'Smooth')
for I,J in enumerate(Cas['Tracking']):
    if not J:
        Cas['Smooth'][I] = 0.

CasP['Smooth'] = New_Plot(Cas['Time'],Cas['Smooth'])
Add_Labels(CasP['Smooth'], 'Smoothed data for Cas-a', *VT_Labels)



# Clip Data
Clip_Data(Cas,5000,35000)
Cas_Mean = np.mean(np.abs(Cas['Smooth']))
for I,J in enumerate(Cas['Smooth']):
    if np.abs(J) > 10.0*Cas_Mean:
        Cas['Smooth'][I] = 0
        
Save_Data(Cas,'Clipped')

CasP['Clip'] = New_Plot(Cas['Time'],Cas['Smooth'],'green')
Add_Labels(CasP['Clip'], 'Fitted selection of data from Cas-a', *VT_Labels)
ax = plt.gca()
ax.set_xlim([5000,35000])
    
## Making the fit
Cas['Ra'] = np.radians(351.007098417797)
Cas['Dec'] = np.radians(58.8924752797345)
Cas['Hs'] = np.radians(Cas['LST']) - Cas['Ra']
    
# X,Hs = Basis_Functions(Cas['Sin_Hs'], Cas_Dec, Baseline):
Cas['Baselines'],Cas['S_sq'],Cas_Min,CasS =  Relevant_Stats(Cas['Hs'],Cas['Dec'],Cas['Smooth'],True)

plt.plot(Cas['Time'],CasS['Y_Fit'],color='red')
CasP['Baseline'] = New_Plot(Cas['Baselines'],Cas['S_sq'],'red')


Add_Labels(CasP['Baseline'], 'Fit Error vs. Dec for Cas-a',
    'Declination (Radians)','Error '+r'$\sigma^2$',Sci=False)
plt.plot(Cas_Min[0],Cas_Min[1],'go')

for Item in CasP:
    Save_PNG_Plot(CasP[Item],'Cas-a_'+Item)