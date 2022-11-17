import pymongo
import bridge
from bridge import identificarPlaca, identificador
monitor = []
client = pymongo.MongoClient("mongodb://administrador:smartgrowing2035@ac-v7suhqb-shard-00-00.50oba8q.mongodb.net:27017,ac-v7suhqb-shard-00-01.50oba8q.mongodb.net:27017,ac-v7suhqb-shard-00-02.50oba8q.mongodb.net:27017/?ssl=true&replicaSet=atlas-53ex9n-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['smartgrowdb']
users = db['usuarios']
datasensores = db['infosensores']
consolidacion = []

def realtimeInterfaz(dispositivo):
    conexion = False
    bridge.interfazRead(dispositivo)
    if bridge.receptInterfaz(dispositivo):
        conexion = True
    return conexion

def updateSensorInterfaz(dispositivo):
    if realtimeInterfaz(dispositivo):
        print(bridge.aux[0])
        #confirmacionPlaca()
        datasensores.update_one(
    {"num_placa": 12345},
    {"$set":{"magnis":[
        bridge.aux[0]]
    }})
    return datasensores

def validarUsuario(x,y):
    registro = False
    verificar = []
    query = users.find_one(
        {"correo": x,
        "password": y}
    )
    verificar.append(query)
    if len(verificar) == 1:
        registro = True
        verificar.clear()
    return registro

def validarPlaca(numero):
    registro = False
    verificar = []
    query = datasensores.find_one(
        {"num_placa": numero}
    )
    verificar.append(query)
    if len(verificar) ==1:
        registro = True
        verificar.clear()
    return registro

def confirmacionPlaca():
    if identificarPlaca:
        signal = bridge.identificador[0]
        consolidacion.clear()
        consolidacion.append(signal)
    return consolidacion

def infoRealtime():
    conexion = False
    bridge.arduinoRead()
    if bridge.receptJson():
        conexion = True
    return conexion

def updateSensor():
    if infoRealtime:
        datasensores.update_one(
    {"num_placa": 12345},
    {"$set":{"magnis":[
        bridge.aux[0]]
    }})
    return datasensores


# IMPLEMENTACIONES FUTURAS

#dispositivo = interfaz.opcionConexion.get()
#usuario = interfaz.textoUsuario.get()
#password= interfaz.textoPass.get()

#users.insert_one(
#    {"correo": "rodrigo",
#    "password": "pruebas"}  
#)

#datasensores.insert_one(
#    {"num_placa": 12345,
#    "magnis": [
#    {
#      "temp": 22,
#      "acid": 0
#    }
#  ]})

#def validarPlaca(num):
#    registro = False
#    if datasensores.find_one({"num_placa": num})

#updateSensor()

