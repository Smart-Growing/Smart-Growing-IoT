import pymongo
import controller
monitor = []
client = pymongo.MongoClient("mongodb://administrador:smartgrowing2035@ac-v7suhqb-shard-00-00.50oba8q.mongodb.net:27017,ac-v7suhqb-shard-00-01.50oba8q.mongodb.net:27017,ac-v7suhqb-shard-00-02.50oba8q.mongodb.net:27017/?ssl=true&replicaSet=atlas-53ex9n-shard-0&authSource=admin&retryWrites=true&w=majority")
mongodb = client['smartgrowdb']
datasensores = mongodb['infosensores']
toFire = {}

def mongoRealtime():
    conexion = False
    controller.arduinoRead()
    if controller.recepJson():
        conexion = True
    return conexion

def mongoUpdate():
    if mongoRealtime:
        datasensores.update_one(
    {"num_placa": 12345},
    {"$set":{"magnis":[
        controller.aux[0]]
    }})
    return datasensores

# Ubicación del array

def fetchingData():
    fireArray = []
    fireJson = {}
    toFire = datasensores.find_one( {}, { "magnis": {"$elemMatch": {"temp": {"$gt": 0}}}})
    fireArray = toFire['magnis']
    fireJson = str(fireArray[0])
    fetchData = fireJson[9:11]
    print(toFire['magnis'])
    print(fireArray[0])
    print(fetchData)
    return fetchData


#mongoRealtime()
#mongoUpdate()
#fetchingData()




    