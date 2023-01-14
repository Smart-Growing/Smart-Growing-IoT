import json
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app, get_app, delete_app
registros = []

try:
    default_app = get_app()
except ValueError:
    default_app = initialize_app()

db = firestore.client()

def crearJson():
    collection_names = ['reportes']
    collections = dict()
    dict4json = dict()
    n_documents = 0
    for collection in collection_names:
        collections[collection] = db.collection(collection).get()
        dict4json[collection] = {}
        for document in collections[collection]:
            docdict = document.to_dict()
            dict4json[collection][document.id] = docdict
            n_documents += 1

    jsonfromdict = json.dumps(dict4json, indent=4, sort_keys=True, default=str)
    #json.dumps(my_dictionary, indent=4, sort_keys=True, default=str)

    path_filename = "Reportes/Historico.json"
    print ( len(collection_names), n_documents, len(jsonfromdict), path_filename )
    with open(path_filename, 'w') as the_file:
        the_file.write(jsonfromdict)

reportes_ref = db.collection(u'reportes')
docs = reportes_ref.stream()


def fetchReportes():
    with open("Reportes/Historico.json") as json_file:
        data = json.load(json_file)
        df = pd.DataFrame(data)
        df.to_excel('Reportes/ReporteHistorico.xlsx')


try:
    delete_app(default_app)
except ValueError:
    pass


# add your collections manually
#cred = credentials.Certificate("sdk.json")

#firebase_admin.initialize_app(cred)

#comportamiento = docs
#    for doc in comportamiento:
#        doc_dict = doc.to_dict()
#        registros.append(doc_dict)
#        return registros