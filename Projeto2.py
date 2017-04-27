#cinética das diferentes anfetaminas
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

dose_total = 20
doseCP = dose_total/2
doseLP = dose_total/2
Z = [doseCP, 0, 0] #condição inicial
Z0 = [10, 0, 0]
elimD = 0.4
elimS = 0.4
elimN = 0.3
absD = 0.6
absS = 0.6

listaT = np.arange(0,10,1e-5)

def estoquesCP(Z, t):
    D = Z[0]
    S = Z[1]
    N = Z[2]
    
    dDdt = - elimD*D - absD*S

    dSdt = absd*D - elimS*S - absS*S

    dNdt = absS*S - elimN*N
    
    return ([dDdt, dSdt, dNdt])



a= odeint(estoques, Z0, listaT)

plt.plot(listaT, a[:,0],label="Sist. digestivo")
plt.legend()
plt.plot(listaT, a[:,1],label="Sist. sanguíneo")
plt.legend()
plt.plot(listaT, a[:,2],label="Sist. nervoso")
plt.legend()
plt.grid(True)
plt.xlabel("Tempo [s]")
plt.ylabel("Concentração [mg/L]")
plt.show()