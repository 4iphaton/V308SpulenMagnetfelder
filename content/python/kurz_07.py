import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

xi, Bi = np.genfromtxt('content/values/Spulek_0,7i.txt',unpack=True)
xi = xi - 3
xi = xi / 100
Bi = Bi / 1000
xal, Bal = np.genfromtxt('content/values/Spulek_0,7al.txt',unpack=True)
xal = xal - 8
xal = xal / 100
Bal = Bal / 1000
xar, Bar = np.genfromtxt('content/values/Spulek_0,7ar.txt',unpack=True)
xar = xar + 4
xar = xar / 100
Bar = Bar / 1000
Nl = 100
ll = 5.5 / 100
mur = 1
mu0= 4 * np.pi * 10**(-7)
I1 = 0.7
R = 41 /1000
#Theoriekurve

Bit = (mur * mu0 * Nl * I1)/ll
Bat = Nl * 4 * np.pi* 10**(-7) * (I1/2)* (R**2/((R**2 + (xal)**2)**(3/2)))
def fa(x):
    return( Nl * 4 * np.pi * 10**(-7) * (I1/2)* (R**2/((R**2 + (x)**2)**(3/2))))
def fi(x):
    return((mur * mu0 * Nl *(x/x)* I1)/ll)
print(Bit)
print(Bat)
ln= np.linspace(-0.03, 0.03, 5000)
#ln2= np.linspace(-0.08, -0.03, 5000)
ln2= np.linspace(-0.08, 0.09, 5000)
ln3= np.linspace(0.03, 0.09, 5000)
ln4= np.linspace(-0.08, -0.03, 5000)
#ln2 = np.linspace(xa[0],xa[len(xa)-1],5000)

#plt.plot(ln4, fa(ln4), 'g-', label='linksseitig außen')#'Theoriekurve linksseitig außen')
#plt.plot(ln3, fa(ln3), 'y-', label='rechtsseitig außen')#'Theoriekurve rechtsseitig außen')
plt.plot(ln2, fa(ln2), 'g-', label='Biot-Savart')
#plt.plot(ln, fa(ln), 'k-', label='Theoriekurve innen (Biot-Savart) ')
plt.plot(ln, fi(ln), 'k-', label='lange Spule')
#plt.plot(ln, Bin(ln, *parameters), 'g-', label='Fit')
plt.plot(xi,Bi,'rx',label='innen')
plt.plot(xal,Bal,'bx',label='linksseitig außen')
plt.plot(xar,Bar,'cx',label='rechtsseitig außen')#Messwerte rechtsseitig außen')
plt.xlabel(r'$x / m$')
plt.ylabel(r'$B / T$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot3.pdf')
print('----------------')
