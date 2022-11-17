import time
from pyserial import serial
aux = []
identificador = []

def interfazRead(dispositivo):
    arduino = serial.Serial(dispositivo,9600)
    time.sleep(5)
    sensores = arduino.readline().strip()
    cleanData = eval(sensores.decode("utf-8"))
    arduino.close()
    aux.append(cleanData)

def identificarPlaca(microcontrolador):
    coherencia = False
    if len(identificador) == 1:
        identificador.clear()
        identificador.append(microcontrolador)
        coherencia = True
    else:
        identificador.append(microcontrolador)
        coherencia = True
    return coherencia

def receptInterfaz(dispositivo):
    existencia = False
    interfazRead(dispositivo)
    if len(aux) == 1:
        existencia = True
        print(aux)
        aux.clear()
    return existencia

def receptJson():
    existencia = False
    arduinoRead()
    if len(aux) == 1:
        existencia = True
        print(aux)
    return existencia

def arduinoRead():
    arduino = serial.Serial('COM3', 9600)
    time.sleep(1)
    sensores = arduino.readline().strip()
    cleanData = eval(sensores.decode("utf-8"))
    arduino.close()
    aux.append(cleanData)

