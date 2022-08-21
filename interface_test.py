import nidaqmx
import time
import numpy as np
import matplotlib.pyplot as plt

Tstop = 25 # Logging Time [seconds]
Ts = 5# Sampling Time [seconds]
data = [0,4,12,17,0]
t = np.arange(0,Tstop,Ts)
plt.plot(t,data, "-o")
plt.title('Curvas Características')
plt.xlabel('Tensão [V]')
plt.ylabel('Potência [W]')
plt.grid()
Tmin = 0; Tmax = 20
plt.axis([0, Tstop, Tmin, Tmax])
plt.show()