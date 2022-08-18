# before start commands     
# pip install nidaqmx
# ==============================================#

from unittest.mock import DEFAULT
import nidaqmx

task = nidaqmx.Task()

task.ai_channels.add_ai_voltage_chan("dev1/ai0")    

task.start()

value = task.read()

print(value)

task.stop()

task.close()

#dev1/ai0