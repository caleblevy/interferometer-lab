Cyg = Data['Cygnus-a']
CygP = {}

CygP['Raw'] = New_Plot(Cyg['Time'],Cyg['Voltage'],'purple')
Add_Labels(CygP['Raw'],'Raw data for the Cygnus-a on 03-25', *VT_Labels)
plt.gca().set_xlim([0,len(Cyg['Voltage'])])

Cyg['Smooth'] = BoxCar_Smooth(Cyg['Voltage'])
for I,J in enumerate(Cyg['Tracking']):
    if not J:
        Cyg['Smooth'][I] = 0.
        
CygP['Smooth'] = New_Plot(Cyg['Time'],Cyg['Smooth'])
Add_Labels(CygP['Smooth'],'Smooth data for the Cygnus-a on 03-25', *VT_Labels)


Clip_Data(Cyg,3000,20000)
CygP['Clip'] = New_Plot(Cyg['Time'],Cyg['Smooth'],'purple')
Add_Labels(CygP['Clip'], 'Fitted selection of data from Cygnus-a', *VT_Labels)
ax = plt.gca()
ax.set_xlim([3000,20000])

Cyg['Ra'] = np.radians(299.991066090114)
Cyg['Dec'] = np.radians(40.546238043595)
Cyg['Hs'] = np.radians(Cyg['LST']) - Cyg['Ra']

Cyg['Baselines'],Cyg['S_sq'],Cyg_Min,CygS =  Relevant_Stats(Cyg['Hs'],Cyg['Dec'],Cyg['Smooth'])

plt.plot(Cyg['Time'],CygS['Y_Fit'],color='orange')
CygP['Baseline'] = New_Plot(Cyg['Baselines'],Cyg['S_sq'],'red')


Add_Labels(CygP['Baseline'], 'Fitting Error vs. Baseline for Cygnus-a',
    'Baseline (Meters)','Error '+r'$\sigma^2$',Sci=False)
plt.plot(Cyg_Min[0],Cyg_Min[1],'go')

Save_Data(Cyg,'Processed')
for Item in CygP:
    Save_PNG_Plot(CygP[Item],'Cygnus-a_'+Item)


