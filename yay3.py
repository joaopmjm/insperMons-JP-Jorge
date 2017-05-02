#cinética das diferentes anfetaminas
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

dose_total = 20
doseCP = dose_total/2
doseLP = dose_total/2
Z = [doseCP, 0, 0] #condição inicial
Z0 = [5, 0, 0]

elimDI = 1.2
elimSI = 1
elimNI = 1
absDI = 1.8
absSI = 1.4
absNI = 0.8

listaT = np.arange(0,10,1e-5)

def estoquesI(Z, t):
    D = Z[0]
    S = Z[1]
    N = Z[2]
    
    dDdt = - elimDI*D

    dSdt = absDI*D - elimSI*S - absSI*S

    dNdt = absSI*S - elimNI*N
    
    return ([dDdt, dSdt, dNdt])



a= odeint(estoquesI, Z0, listaT)

plt.plot(listaT, a[:,0],"--",label="Sist. digestivo")
plt.plot(listaT, a[:,1],"-.",label="Sist. sanguíneo")
plt.plot(listaT, a[:,2],label="Sist. nervoso")
plt.legend()
plt.grid(True)
plt.title("Droga de ação imediata")
plt.xlabel("Tempo [h]")
plt.ylabel("Concentração [mg/L]")
plt.show()


########################################################################################################################

#cinética das diferentes anfetaminas
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

dose_total = 20
Z = [doseCP, 0, 0] #condição inicial
Z0 = [5, 0, 0]

elimDL = 1.2
elimSL = 1
elimNL = 1
absDL = 1.8
absSL = 1.9
absNL = 0.8

listaT = np.arange(3,10,1e-5)

def estoquesL(Z, t):
    D = Z[0]
    S = Z[1]
    N = Z[2]
    
    dDdt = - elimDL*D 

    dSdt = absDL*D - elimSL*S - absSL*S

    dNdt = absSL*S - elimNL*N

    return ([dDdt, dSdt, dNdt])



b= odeint(estoquesL, Z0, listaT)

plt.plot(listaT, b[:,0],"--",label="Sist. digestivo")
plt.plot(listaT, b[:,1],"-.",label="Sist. sanguíneo")
plt.plot(listaT, b[:,2],label="Sist. nervoso")
plt.legend()
plt.grid(True)
plt.title("Droga de ação retardada")
plt.xlabel("Tempo [h]")
plt.ylabel("Concentração [mg/L]")
plt.show()


########################################################################################################################

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

Z0 = [5, 0, 0] #condição inicial

elimDI = 1.2
elimSI = 1
elimNI = 1
absDI = 1.8
absSI = 1.4
absNI = 0.8

listaT = np.arange(0,10,1e-5)

def estoquesI(Z, t):
    D = Z[0]
    S = Z[1]
    N = Z[2]
    
    dDdt = - elimDI*D

    dSdt = absDI*D - elimSI*S - absSI*S

    dNdt = absSI*S - elimNI*N
    
    return ([dDdt, dSdt, dNdt])



a= odeint(estoquesI, Z0, listaT)

plt.plot(listaT, a[:,2],color="g",label="Sist. nervoso")
plt.legend()
plt.grid(True)
plt.title("Ação das drogas simultâneamente")
plt.xlabel("Tempo [h]")
plt.ylabel("Concentração [mg/L]")



Z0 = [5, 0, 0]

elimDL = 1.2
elimSL = 1
elimNL = 1
absDL = 1.8
absSL = 2.0
absNL = 0.8

listaT2 = np.arange(5,10,1e-5)

def estoquesL(Z, t):
    D = Z[0]
    S = Z[1]
    N = Z[2]
    
    dDdt = - elimDL*D 

    dSdt = absDL*D - elimSL*S - absSL*S

    dNdt = absSL*S - elimNL*N

    return ([dDdt, dSdt, dNdt])



b= odeint(estoquesL, Z0, listaT2)

plt.plot(listaT2, b[:,2],color="g")
plt.legend()
plt.show()
