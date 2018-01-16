import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

xv, Bi, xs = np.genfromtxt('content/values/hh_2,5a.txt',unpack=True)
xs = xs - (6.25/2)
xs = xs /100
Bi = Bi / 1000
#xa, Ba = np.genfromtxt('content/values/Spulel_0,7a.txt',unpack=True)
#xa = xa - 13
#xa = xa / 100
#Ba = Ba / 1000
Nl = 100
mur = 1
mu0= 4 * np.pi * 10**(-7)
I1 = 2.5
Rh = 6.25/100
#Theoriekurve

def fa(x):
    return( (Nl *mu0 * I1 * Rh**(2))/((Rh**(2) + x**2)**(3/2)))
ln= np.linspace(0.035, 0.09 , 5000)

plt.plot(ln, fa(ln), 'g-', label='Theoriekurve außen')
#plt.plot(ln, Bin(ln, *parameters), 'g-', label='Fit')
#plt.plot(xi,Bi,'rx',label='Messwerte innen')
plt.plot(xs,Bi,'bx',label='Messwerte außen')
plt.xlabel(r'$x / m$')
plt.ylabel(r'$B / T$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot6.pdf')
print('----------------')
