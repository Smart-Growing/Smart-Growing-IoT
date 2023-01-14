
import firebase_admin
from firebase_admin import credentials, firestore
import random
import datetime
import mongoclean
from mongoclean import fetchingData
import json
import pandas as pd
registros = []

cred = credentials.Certificate("./resources/sdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

current = datetime.datetime.now()



monitor_ref = db.collection(u'dispositivos').document(u'BZmp9hDRQqdeIRwZHrBH')

reportes_ref = db.collection(u'reportes')

#NUEVA


def generarReportes():
    registro = fetchingData()
    randomAcid = str(random.randint(6,9))
    data = {"placa": 1001, "temp": registro, "acid": randomAcid, "fecha": current}
    print(data)
    reportes_ref.add(data)

# Reportes comportamiento

def obtenerReportes():
    reportes = db.collection(u'reportes').stream()
    for doc in reportes:
        print(f'{doc.id} => {doc.to_dict()}')



def updateFirestore():
    realTemp = fetchingData()
    randomAcid = str(random.randint(6,9))
    data = {"temp": realTemp, "acid": randomAcid}
    print(data)
    monitor_ref.update(data)

# COLLECTION PARA TESTEO DE FUNCIONALIDADES
#monitor_ref = db.collection(u'testeo').document(u'monitortesting')

# COLLECTION PARA IMPLEMENTACION DE LA APP (AUN CON ERRORES EN EL RECYCLERVIEW)
#monitor_ref = db.collection(u'dispositivos').document(u'monitorfuncional')
#BZmp9hDRQqdeIRwZHrBH
#Wey9lU8eJ0S06i2S1yeH

#def actualizarDatos(temp,acid):
#    data = {"temp": temp, "acid": acid}
#    monitor_ref.update(data)

#def convertirJson():
#    converter = False
#    fetchReportes()
#    if len(firestore.registros):
#        with open(firestore.historico) as json_file:
#            data = json.load(json_file)
#            df = pd.DataFrame(data)
#            df.to_excel('./ReporteHistorico.xlsx')

# ORDEN DE LAS FUNCIONES PARA MULTITASKING

#mongoclean.mongoRealtime()
#mongoclean.mongoUpdate()
#fetchingData()
#updateFirestore()

