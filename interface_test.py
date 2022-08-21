import nidaqmx
import time
import numpy as np
import matplotlib.pyplot as plt

Tstop = 10 # Logging Time [seconds]
Ts = 1 # Sampling Time [seconds]
data = [1,2,2,1,3,4,5,6,10,3]
t = np.arange(0,Tstop,Ts)
plt.plot(t,data, "-o")
plt.title('Temperature')
plt.xlabel('t [s]')
plt.ylabel('Temp [degC]')
plt.grid()
Tmin = 0; Tmax = 10.5
plt.axis([0, Tstop, Tmin, Tmax])
plt.show()