import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

xi, Bi = np.genfromtxt('content/values/Spulel_0,7i.txt',unpack=True)
xi = xi * 100
Bi = Bi * 1000
xa, Ba = np.genfromtxt('content/values/Spulel_0,7a.txt',unpack=True)
xa = xa / 100
Ba = Ba / 1000
Nl = 300
ll = 16 / 100
mur = 1
mu0= 4 * np.pi * 10**(-7)
I1 = 0.7
R = 41 /1000
#Theoriekurve

Bin = (mur * mu0 * Nl * I1)/ll )
Bat = 4 * np.pi * (I1/2)* (R**2/(R**2 + xa**2)**(3/2))

ln = np.linspace(xi[0],xi[len(t)-1],5000)

plt.plot(xa, Bat, 'g-', label='Theoriekurve innen ')
plt.plot(xi, Bit, 'g-', label='Theoriekurve außen')
#plt.plot(ln, Bin(ln, *parameters), 'g-', label='Fit')
plt.plot(xi,Bi,'rx',label='Messwerte innen')
plt.plot(xa,Ba,'bx',label='Messwerte außen')
plt.xlabel(r'$x / m$')
plt.ylabel(r'$B / T$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1.pdf')
print('----------------')
