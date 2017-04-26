#cinética das diferentes anfetaminas
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

tempo=np.arange(0,36000,0.001)
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
tad=0.45  #taxa de absorção da parde intestinal
tas=0.25  #taxa de absorção no sangue para o sistema nervoso
listaT = np.arange(0,10,1e-5)

def f(doseCP,doseLP,tad):   #relação digestio sanguíneo
	return doseCP*tad+doseLP*tad

def g(doseCP,DoseLP,tas):   #relação sangue nervoso
	return doseCP*tas+doseLP*tas

def estoques(Z, t):
    doseCP = Z[0]
    doseLP = Z[1]
    
    dDdt = - elimDCP*doseCP - elimDLP*doseLP - doseCP*tas+doseLP*tas

    dSdt = doseCP*tas+doseLP*tas - elimSCP*doseCP - elimSLP*doseLP - doseCP*tad+doseLP*tad

    dNdt = doseCP*tad+doseLP*tad - elimNCP*doseCP - elimNLP*doseLP
    
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