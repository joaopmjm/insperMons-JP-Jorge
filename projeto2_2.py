#cinética da administração de 2 doses ao dia (desconciderando as diferentes anfetaminas)
dose_total = 20 #condição inicial
elimD = 
elimS = 
elimN = 

dDdt =- elimD*dose_total - f(D, S)

dSdt = f(D, S) - elimS*dose_total - g(S, N)

dNdt = g(S, N) - elimN*dose_total