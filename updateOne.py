from coneccion import *
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Supermercado

coleccion = db.productos
# documentos = coleccion.find({"nombre":"Cereal"})
filtro = {'ODOO UNI':'708000000'}
update = {"$set":{'CATEG NESTLÉ':'Cookies'}}

# updateDocumento = coleccion.update_one()

try:
    modificacion =coleccion.update_one(filtro,update) 
    print("act realizada")
except Exception as e:
    print(e)