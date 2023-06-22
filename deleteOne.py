from coneccion import *
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Supermercado
coleccion = db.productos

filtro = {'ODOO UNI':'708000000'}

try:
    modificacion = coleccion.delete_one(filtro)
    print('accion realizada')
except Exception as e:
    print(e)

# Funciona!!