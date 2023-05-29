from coneccion import *

db = client.Supermercado

coleccion = db.productos
# documentos = coleccion.find({"nombre":"Cereal"})
filtro = {'nombre':'Cereal'}
update = {"$set":{'precio':'6.99'}}

# updateDocumento = coleccion.update_one()

try:
    modificacion =coleccion.update_one(filtro,update) 
    print("act realizada")
except Exception as e:
    print(e)