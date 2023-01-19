
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



