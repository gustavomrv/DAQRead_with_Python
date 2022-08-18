# before start commands     
# pip install nidaqmx
# ==============================================#

from unittest.mock import DEFAULT
import nidaqmx

task = nidaqmx.Task()

task.ai_channels.add_ai_voltage_chan("dev4/ai0", "myAIChannel", terminal_config=DEFAULT, min_val=-5, max_val=5, VoltageUnits = VoltageUnits.VOLTS)

task.start()

value = task.read()

print(value)

task.stop()

task.close()

#dev1/ai0