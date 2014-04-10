#!/usr/bin/env python
import numpy as np
import scipy as sp
import pylab as plt
import math
execfile('Graph_Atoms.py')




def draw_line(x,y,angle,length):
  cartesianAngleRadians = (450-angle)*math.pi/180.0
  terminus_x = x + length * math.cos(cartesianAngleRadians)
  terminus_y = y + length * math.sin(cartesianAngleRadians)
  plt.plot([x, terminus_x],[y,terminus_y])
  print [x, terminus_x],[y,terminus_y]


# pl.axis('equal')
# pl.axis([-5,20,-5,40])


Arrows = plt.figure(figsize=(22.,10.))

x_lim = 25.
y_lim = 2.0

r = 8.
x_0 = x_lim+r-1.5
y_0 = 0.
N_Points = 100
N_Angs = 11

def Circle_Points(r,x_0,y_0,N_Points=100):
    theta = np.linspace(0.,np.pi*2,N_Points)
    Circ_Points = r*np.exp(1j*theta)+ x_0 + 1j*y_0
    return np.real(Circ_Points),np.imag(Circ_Points)
    
x_circ,y_circ = Circle_Points(r,x_0,y_0)
plt.plot(x_circ,y_circ,'yellow',linewidth=4.0)


angles = np.array([-60,-70,-80,-90,-100,-110,-120]*N_Angs)
x = []
y = []
for I in range(N_Angs):
    x += [x_circ[N_Points/2-(N_Angs-1)/2+I]]*7
    y += [y_circ[N_Points/2-(N_Angs-1)/2+I]]*7
    
x = np.array(x)
y = np.array(y)
print y_circ
ax = plt.gca()
ax.set_xlim([0.,x_lim])
ax.set_ylim([-y_lim,y_lim])



for i in range(0,len(x)):
    print x[i],y[i],angles[i]
    draw_line(x[i],y[i],angles[i],25)
    
# r_e = 1.0
# x_e = -0.5
#     
# Earth_x,Earth_y = Circle_Points(r_e,x_e,0.)
# plt.plot(Earth_x,Earth_y,'blue',linewidth=100.0)
# plt.add_patch(Earth_x,Earth_)
ax.add_patch(plt.Circle((-0.5,0),1,color='blue',zorder=5))
# ax.add_patch(plt.Circle((x_0,y_0),r,color='yellow'))
X_IntersectB = 0.4673
Y_IntersectB = 0.253976

X_IntersectT = 0.15046
Y_IntersectT = 0.760145

Z_B = X_IntersectB + 1j*Y_IntersectB
Z_T_Diff = X_IntersectB + 1j*Y_IntersectT
Z_to_Plot(Base_Line(Z_B,Z_T_Diff))
Z_T = X_IntersectT+1j*Y_IntersectT
z = Base_Line(Z_T,Z_T_Diff)
x_Base,y_Base = Z_to_XY(z)
plt.plot(x_Base,y_Base,color='black',linewidth=3.0)

def No_Ax(Fig):
    plt.figure(Fig.number)
    ax = plt.gca()
    plt.setp( ax.get_xticklabels(), visible=False)
    plt.setp( ax.get_yticklabels(), visible=False)
    plt.setp( ax.get_xticklines(), visible=False)
    plt.setp( ax.get_yticklines(), visible=False)
    
No_Ax(Arrows)
plt.plot(x_circ,y_circ,'brown',linewidth=4.0)
ax.add_patch(plt.Circle((x_0,y_0),r,color='orange'))

plt.plot([X_IntersectB],[Y_IntersectB],'ro',zorder=7)
plt.plot([X_IntersectT],[Y_IntersectT],'ro',zorder=7)
plt.plot([X_IntersectB],[Y_IntersectT],'go',zorder=7)


plt.title('Collimation of Light from a Far-Away Source',fontsize=30)
plt.savefig("Collimation.pdf",bbox_inches='tight')

ax.set_xlim([0,1.5])
ax.set_ylim([-1.5,1.5])
  
plt.show()