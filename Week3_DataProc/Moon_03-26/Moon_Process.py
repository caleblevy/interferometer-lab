Moon = Data['Moon']
MoonP = {}

MoonP['Raw'] = New_Plot(Moon['Time'],Moon['Voltage'],'purple')
Add_Labels(MoonP['Raw'],'Raw voltage data for Moon on 03-26', *VT_Labels)


Moon['Smooth'] = BoxCar_Smooth(Moon['Voltage'])
for I,J in enumerate(Moon['Tracking']):
    if not J:
        Moon['Smooth'][I] = 0.
Moon['Smooth'] = BoxCar_Smooth(Moon['Smooth'],100,np.mean)
Moon['Voltage'] = Moon['Smooth']
plt.gca().set_xlim([0,Moon['Time'][len(Moon['Voltage'])-1]])

width = 50
MoonE_P = Find_EnvelopeP(Moon)
MoonE_M = Find_EnvelopeM(Moon)


MoonP['Smooth'] = New_Plot(Moon['Time'],Moon['Smooth'],'purple')
plt.plot(MoonE_P['Time'],MoonE_P['Voltage'],color='blue')
plt.plot(MoonE_M['Time'],MoonE_M['Voltage'],color='red')

Add_Labels(MoonP['Smooth'],'Voltage data for Moon on 03-26', *VT_Labels)
plt.gca().set_xlim([0,Moon['Time'][len(Moon['Voltage'])-1]])

# MoonS_P = Moon_Fit(MoonE_P)
# MoonS_M = Moon_Fit(MoonE_M)
# plt.plot(MoonE_P['Time'],MoonS_P['Y_Fit']+.0002,'orange')
# plt.plot(MoonE_M['Time'],MoonS_M['Y_Fit']+.0002,'orange')
Null_Ind = np.where(np.round(Moon['Time']) == 18000)[0][0]
print Moon['LST'][Null_Ind]

MoonB = {}

MoonB['R'],MoonB['Amp'] = Diameter_Function(Moon,Null_Ind)
MoonB['R'] = np.rad2deg(MoonB['R'])
Save_Data(MoonB,'Bessel')

MoonP['Diam'] = New_Plot(MoonB['R'],MoonB['Amp'],'red')
Add_Labels(MoonP['Diam'],'Moon Modulation Function at the Null Point',
    'Angular Radius (Degrees)','Amplitude',Sci=False)
plt.plot(MoonB['R'],np.zeros(500),color='black')
plt.plot([0.193],[0.],'yo')
plt.gca().set_xlim([0.,0.6])
plt.gca().get_yaxis().set_visible(False)
plt.savefig('Moon_Diameter.pdf')


# MoonE_P['Smooth'] = BoxCar_Smooth(MoonE_P['Voltage'],20,np.mean)
# MoonE_M['Smooth'] = BoxCar_Smooth(MoonE_M['Voltage'],20,np.mean)
# MoonP['Cross'] = plt.figure()
# plt.plot(MoonE_P['Time'],MoonE_P['Smooth'],'blue')
# plt.plot(MoonE_M['Time'],MoonE_M['Smooth'],'red')

for I in MoonP:
    Save_PNG_Plot(MoonP[I],'Moon_'+I)

pylab.show()


# # plt.gca().set_xlim([0,24000])# 
# # Add_Labels(MoonP['Raw'],'Raw voltage data for Moon on 03-26', *VT_Labels)
# # Save_PNG_Plot(MoonP['Raw'],'Moon_Envelope')
# 
# width = 50
# Clip_Data(MoonE_P,19000/width,22000/width)
# Clip_Data(MoonE_M,19000/width,21500/width)
# 
# # MoonS_P,MoonS_M = Resolved_Fit(MoonE_P,MoonE_M)
# Clip_Data(Moon,19000,24000)
# plt.gca().set_xlim([19000,24000])
# [Parab_P,Parab_M] = Interpolate_Fit(MoonE_P,MoonE_M,Moon['Time'])
# plt.plot(Moon['Time'],Parab_P,Moon['Time'],Parab_M,color='purple')
# #plt.plot(MoonE_P['Time'],MoonS_P['Y_Fit'],MoonE_M['Time'],MoonS_M['Y_Fit'],color='purple')
# Add_Labels(MoonP['Raw'],'Null point for Moon voltage data', *VT_Labels)
# Save_PNG_Plot(MoonP['Raw'],'Moon_Null')

