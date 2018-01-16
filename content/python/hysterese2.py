import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

In, Bn = np.genfromtxt('content/values/hys_neu.txt',unpack=True)
Bn = Bn / 1000
Iab, Bab = np.genfromtxt('content/values/hys_abf.txt',unpack=True)
Bab = Bab / 1000
Ian, Ban = np.genfromtxt('content/values/hys_ans.txt',unpack=True)
Ban = Ban / 1000
mu0= 4 * np.pi * 10**(-7)
r = 3 / 2000

def H(I):
    return( I*595/(2*np.pi*r) )

print('Remanenz abf:', Bab[11])
print('Remanenz ans:', Ban[11])
print(' Sättigungsmagnetisierung:', Bab[21])
print(' Sättigungsmagnetisierung:', Ban[21])
print('Koerzitivkraft:', H(-0.25))
print('Koerzitivkraft:', H(0.32))

#plt.plot(ln, fa(ln), 'g-', label='Theoriekurve innen')
#plt.plot(ln, Bin(ln, *parameters), 'g-', label='Fit')
#plt.plot(xi,Bi,'rx',label='Messwerte innen')
plt.plot(H(In),Bn,'bx',label='Neukurve')
plt.plot(H(In),Bn,'c-')
plt.plot(H(Iab),Bab,'rx',label='abfallend')
plt.plot(H(Iab),Bab,'m-')
plt.plot(H(Ian),Ban,'kx',label='ansteigend')
plt.plot(H(Ian),Ban,'g-')
ax = plt.gca()
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axes.set_xlabel(r'$H / T$', fontsize = 9, x = 1, y = 1)
ax.axes.set_ylabel(r'$B / T$', fontsize = 9, x = 1, y = 1)
plt.xlabel(r'$H / T$')
plt.ylabel(r'$B / T$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot10.pdf')
print('----------------')
