import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

xi, Bi = np.genfromtxt('content/values/Spulel_1,4i.txt',unpack=True)
xi = xi - 8
xi = xi / 100
Bi = Bi / 1000
xa, Ba = np.genfromtxt('content/values/Spulel_1,4a.txt',unpack=True)
xa = xa - 13
xa = xa / 100
Ba = Ba / 1000
Nl = 300
ll = 16 / 100
mur = 1
mu0= 4 * np.pi * 10**(-7)
I1 = 1.4
R = 41 /1000
#Theoriekurve

Bit = (mur * mu0 * Nl * I1)/ll
Bat = Nl * 4 * np.pi* 10**(-7) * (I1/2)* (R**2/((R**2 + (xa)**2)**(3/2)))
def fa(x):
    return( Nl * 4 * np.pi * 10**(-7) * (I1/2)* (R**2/((R**2 + (x)**2)**(3/2))))
def fi(x):
    return((mur * mu0 * Nl *(x/x)* I1)/ll)
print(Bit)
print(Bat)
ln= np.linspace(-0.08, 0.05, 5000)
ln2= np.linspace(-0.13, -0.08, 5000)
#ln2 = np.linspace(xa[0],xa[len(xa)-1],5000)

plt.plot(ln2, fa(ln2), 'g-', label='Theoriekurve außen')
#plt.plot(ln, fa(ln), 'k-', label='Theoriekurve innen (Biot-Savart) ')
plt.plot(ln, fi(ln), 'y-', label='Theoriekurve innen')
#plt.plot(ln, Bin(ln, *parameters), 'g-', label='Fit')
plt.plot(xi,Bi,'rx',label='Messwerte innen')
plt.plot(xa,Ba,'bx',label='Messwerte außen')
plt.xlabel(r'$x / m$')
plt.ylabel(r'$B / T$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot2.pdf')
print('----------------')
