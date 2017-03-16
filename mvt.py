# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import sin,pi, radians, cos
vitesse = 10
angle = 35
anglerad = radians(angle)

Cd = 0.0        # Coefficient de trainée
Cm = C = 0.51   # Coefficient de portance (0.45 pour ballon de foot) (0.51 pour balle de tennis)
R = 0.0325       # Rayon de la sphère (cm) (11 pour ballon de foot) (3.25 pour balle de tennis)
m = 0.055       # Poids de la balle (kg) (430 pour ballon de foot) (55 pour balle de tennis)
p = 1.225     # Masse volumique du fluide (kg/m^3) (1.225 pour l'air)
v0 = v = 0.9*vitesse     # Vitesse initiale de la balle / APPROXIMATION DE LA VITESSE
w0 = wy = 500    # Vitesse initiale de rotation de la balle en y / APPROXIMATION VITESSE DE ROTATION
alpha = pi/2      # Angle entre v et w
wx = wz = 0.0			
g = 9.81

#xsecond = -0.5*C*pi*(R**2)*p*v*xprim/m+0.5*pi*(R**3)*p*sin(alpha)*(wy*zprim-wz*yprim)/m
#ysecond = -0.5*C*pi*(R**2)*p*v*yprim/m+0.5*pi*(R**3)*p*sin(alpha)*(wz*xprim-wx*zprim)/m = 0
#zsecond = -g-0.5*C*pi*(R**2)*p*v*zprim/m+0.5*pi*(R**3)*p*sin(alpha)*(wx*yprim-wy*xprim)/m

dt = 0.1
lT=[0]
lX=[0]
lXPrim=[vitesse * cos(anglerad)]
lZ=[1]
lZPrim=[vitesse * sin(anglerad)]

def Xseconde(XPrim, ZPrim, C, R, p, v, wy, alpha):
	return (1/m)*((-0.5*C*pi*R*R*p*v*XPrim) + 0.5*pi*R*R*R*p*sin(alpha)*wy*ZPrim)

def Zseconde(ZPrim, XPrim, C, R, p, v, wy, m, g, alpha):
	return (1/m)*(-m*g-0.5*C*pi*R*R*p*v*ZPrim - 0.5*pi*R*R*R*p*sin(alpha)*wy*XPrim)

def XprimSuiv(XPrim,XSeconde, dt):
    return XPrim+dt*XSeconde

def ZprimSuiv(ZPrim,ZSeconde, dt):
	return ZPrim+dt*ZSeconde

def XSuiv(X,XPrim, dt):
    return X+dt*XPrim 

def ZSuiv(Z,ZPrim, dt):
    return Z+dt*ZPrim
              
def tSuiv(t,dt):
    return t+dt
    
def constructor(lT,lX,lXPrim,lZ,lZPrim,dt,C, R, p, v, wy, m, g, alpha):
    while lZ[-1] >0 :
        lT.append(tSuiv(lT[-1],dt))
        lX.append(XSuiv(lX[-1],lXPrim[-1],dt))
        lZ.append(ZSuiv(lZ[-1],lZPrim[-1],dt))
        lXPrim.append(XprimSuiv(lXPrim[-1],Xseconde(lXPrim[-1],lZPrim[-1], C, R, p, v, wy, alpha), dt))
        lZPrim.append(ZprimSuiv(lZPrim[-1],Zseconde(lZPrim[-1],lXPrim[-1], C, R, p, v, wy, m, g , alpha), dt))
    return lT, lX, lXPrim, lZ, lZPrim


Tuple = constructor(lT,lX,lXPrim,lZ,lZPrim,dt,C, R, p, v, wy, m, g, alpha)
plt.axis([0,20,-2,8])
plt.plot(Tuple[1],Tuple[3])
plt.show()
                  
             
               
 
