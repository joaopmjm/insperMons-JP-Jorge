#cinética das diferentes anfetaminas
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

dose_total = 20
doseCP = 10
doseLP = 10
Z = [doseCP, doseLP] #condição inicial
elimDCP = 0.6
elimDLP = 0.1
elimSCP = 0.4
elimSLP = 0.5
elimNCP = 0.3
elimNLP = 0.8

listaT = np.arange(0,10,1e-5)

def estoques(Z, t):
    doseCP = Z[0]
    doseLP = Z[1]
    
    dDdt = - elimDCP*doseCP - elimDLP*doseLP - f(D, S)

    dSdt = f(D, S) - elimSCP*doseCP - elimSLP*doseLP - g(S, N)

    dNdt = g(S, N) - elimNCP*doseCP - elimNLP*doseLP
    
    return ([dDdt, dSdt, dNdt])

a= odeint(estoques, Z, listaT)

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