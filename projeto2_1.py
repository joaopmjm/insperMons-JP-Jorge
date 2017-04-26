#cinética das diferentes anfetaminas
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
dt=0.1
tempo1=np.arange(0,7200,dt)
tempo2=np.arange(7200+dt,36000,dt)
doseCP = 10
doseLP = 10
dose_totbl = doseCP+doseLP
D=dose_totbl
S=0
N=0
Z0 = [D,S,N] #condição inicibl
elimDCP = 0.005
elimDLP = 0.001
elimSCP = 0.004
elimSLP = 0.005
elimNCP = 0.003
elimNLP = 0.008
tad=0.7  #taxa de absorção da parede intestinbl
tas=0.9  #taxa de absorção no sangue para o sistema nervoso
tun=0.99   #taxa de uso nervoso, quanto o sis. nervoso vai utilisar a cada intervblo de tempo

def  estoquesL(Z,t):
	dDdt = - elimDLP * doseLP + doseLP * tas
	dSdt = doseLP * tas - elimSLP*doseLP + doseLP * tad
	dNdt = doseLP * tad - elimNLP * doseLP
	return (dDdt, dSdt, dNdt)



def estoques1C(Z0, t): #antes de duas horas
	dDdt = - elimDCP * doseCP  - doseCP * tas
	dSdt = doseCP * tas - elimSCP*doseCP - doseCP * tad
	dNdt = doseCP * tad - elimNCP * doseCP
	return (dDdt, dSdt, dNdt)

a= odeint(estoques1C, Z0, tempo1)

Z=[a[len(tempo1)-1][0],a[len(tempo1)-1][1],a[len(tempo1)-1][2]]

a0=a[len(tempo1)-1][0]

bl=odeint(estoquesL,Z,tempo2)




def estoques2C(Z,t):
	dDdt = - elimDCP * doseCP - doseCP * tas
	dSdt = doseCP * tas - elimSCP*doseCP - doseCP * tad
	dNdt = doseCP * tad - elimNCP * doseCP
	return (dDdt, dSdt, dNdt)

bc= odeint(estoques2C,Z,tempo2)

plt.plot(tempo1, a[:,0],label="Sist. digestivo instantâneo")
plt.plot(tempo1, a[:,1],label="Sist. sanguíneo instantâneo")
plt.plot(tempo1, a[:,2],label="Sist. nervoso instantâneo")
plt.plot(tempo2, bc[:,0],label="Sist. digestivo instantâneo após 2h")
plt.plot(tempo2, bc[:,1],label="Sist. sanguíneo instantâneo após 2h")
plt.plot(tempo2, bc[:,2],label="Sist. nervoso instantâneo após 2h")
plt.plot(tempo2, bl[:,0],label="Sist. digestivo lento após 2h")
plt.plot(tempo2, bl[:,1],label="Sist. sanguíneo lento após 2h")
plt.plot(tempo2, bl[:,2],label="Sist. nervoso lento após 2h")
plt.legend()
plt.grid(True)
plt.xlabel("Tempo [s]")
plt.ylabel("Concentração [mg/L]")
plt.show()

# dois odeints, com as equações de cada intervblo de tempo
