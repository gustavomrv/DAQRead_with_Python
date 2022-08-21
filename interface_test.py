import nidaqmx
import time
import numpy as np
import matplotlib.pyplot as plt

#Tstop = 25 # Logging Time [seconds]
#Ts = 5# Sampling Time [seconds]
#data = [0,4,12,17,0]
#t = np.arange(0,Tstop,Ts)

tensao = []
potencia = []

for i in range(0,25,1):
    tensao.append(i)
    potencia.append(i*i)

# plt.plot(t,data, "-o")
plt.plot(tensao,potencia, "")
plt.title('Curvas Características')
plt.xlabel('Tensão [V]')
plt.ylabel('Potência [W]')
# plt.grid()

print(max(tensao))
print(max(potencia))

# Tmin = 0; Tmax = potencia[24]

plt.axis([0, max(tensao) + 6, 0, max(potencia)+100])
plt.show()