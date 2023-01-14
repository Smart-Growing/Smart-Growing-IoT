import time
from pyserial import serial
aux = []


def arduinoRead():
    arduino = serial.Serial('COM3',9600)
    time.sleep(1)
    sensores = arduino.readline().strip()
    cleanData = eval(sensores.decode("utf-8"))
    arduino.close()
    aux.append(cleanData)

def recepJson():
    existencia = False
    arduinoRead()
    if len(aux) == 1:
        existencia = True
        print(aux)
    return existencia






