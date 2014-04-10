#!/usr/bin/env python
execfile('Data_Process.py')

Voltage = Data['Voltage']
Time = Data['Time']

def New_Plot(*args):
    Fig = plt.figure()
    plt.plot(*args)
    return Fig

Data_Fig = plt.figure()

N_Points = len(Voltage)
Delta = [Time[I+1]-Time[I] for I in xrange(N_Points-1)]
Delta_Plot = plt.figure()
plt.plot(Time[:-1],Delta)
#print dt
#print Time[1] - Time[0]
# pylab.ion()
# Delta_Plot.show()
plt.figure(Data_Fig.number)
plt.plot(Time,Voltage)
# pylab.show()
