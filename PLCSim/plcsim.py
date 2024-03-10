import snap7
from snap7.util import *
from scipy import signal
import time 
import math
import matplotlib.pyplot as plt
import numpy as np


plc = snap7.client.Client()
plc.connect('192.168.0.1',0,1)
print('connected')

while True:
    time.sleep(0.1)
    valor = time.sleep(0.1)
    print(valor, " ")

    # mb para memoria (lectura de memoria)
    #marca = plc.mb_read(0,1)
    #marca1 = get_byte(marca,0)
    #print('Marca',marca1) 
    x = int(math.sin(2*math.pi*valor))



    # escribir en la entrada analogica MW1
    MW1 = plc.mb_read(1,2)
    set_int(MW1, 0, x)
    plc.mb_write(1, 2, MW1)


    MW1 = plc.mb_read(1,2)
    SensorNivelPLC = get_int(MW1,0)
    print(' SensorNivelPLC : ',  SensorNivelPLC) 


    #"ab" para salidas (lectura de salida digital)
     #SalidaQ0 = plc.ab_read(0,1)
     #SalidaQ0_1 = get_bool(SalidaQ0, 0, 1)
     #print(' Salida Q0.1:', SalidaQ0_1)

    # escribir salida digital
    #Q0 = plc.ab_read(0,1)
    #set_bool(Q0,0,1,0)
    #plc.ab_write(0,Q0)

    #Leer la intrada analogica IW0 
    #IW_2 = plc.eb_read(2,2)
    #IW_2_int = get_int(IW_2,0)
    #print(' IW2 : ', IW_2_int )

    # escribir entrada digital
    #I0 = plc.eb_read(0,1)
    #set_bool(I0,0,0,1)
    #plc.eb_write(0,1,I0)











    

