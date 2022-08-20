# before start commands     
# pip install nidaqmx
# ==============================================#
import nidaqmx

taskvolt = nidaqmx.Task()
taskamp = nidaqmx.Task()

taskvolt.ai_channels.add_ai_voltage_chan("dev1/ai0")    
taskamp.ai_channels.add_ai_current_chan("dev1/ai0") 

taskvolt.start()
taskamp.start()

valuevolt = taskvolt.read()
valueamp = taskamp.read()

print(valuevolt)
print(valueamp*valuevolt)

taskvolt.stop()
taskamp.stop()

taskvolt.close()
taskamp.close()

#dev1/ai0