from coneccion import *

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Supermercado

# codigo = input("ingrese el codigo del producto")

coleccion = db.productos
documentos = coleccion.find({"ODOO UNI":"708000000"})

for documentos in documentos:
    print(documentos)

# ya no funciona!!!