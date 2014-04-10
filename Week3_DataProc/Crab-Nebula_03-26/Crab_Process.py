Crab = Data['Crab-Nebula']
CrabP = {}

CrabP['Raw'] = New_Plot(Crab['Time'],Crab['Voltage'])
Add_Labels(CrabP['Raw'],'Raw data for the Crab Nebula on 03-26', *VT_Labels,Sci='off')
plt.gca().set_xlim([0,len(Crab['Voltage'])])

Crab['Smooth'] = BoxCar_Smooth(Crab['Voltage'])
for I,J in enumerate(Crab['Tracking']):
    if not J:
        Crab['Smooth'][I] = 0.
        
CrabP['Smooth'] = New_Plot(Crab['Time'],Crab['Smooth'])
Add_Labels(CrabP['Smooth'],'Smooth data for the Crab Nebula on 03-26', *VT_Labels,Sci='off')

Crab['Ra'] = np.radians(83.8490115899214)
Crab['Dec'] = np.radians(22.0209899205629)
Crab['Hs'] = np.radians(Crab['LST']) - Crab['Ra']

Crab['Baselines'],Crab['S_sq'],Crab_Min,CrabS =  Relevant_Stats(Crab['Hs'],Crab['Dec'],Crab['Smooth'])

plt.plot(Crab['Time'],CrabS['Y_Fit'],color='yellow')
plt.gca().set_xlim([0,len(Crab['Voltage'])])

CrabP['Baseline'] = New_Plot(Crab['Baselines'],Crab['S_sq'],'red')



Add_Labels(CrabP['Baseline'], 'Fitting Error vs. Baseline for Crab Nebula',
    'Baseline (Meters)','Error '+r'$\sigma^2$',Sci=False)
plt.plot(Crab_Min[0],Crab_Min[1],'go')


Save_Data(Crab,'Processed')
for Item in CrabP:
    Save_PNG_Plot(CrabP[Item],'Crab_'+Item)







