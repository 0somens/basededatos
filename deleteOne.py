from coneccion import *

db = client.Supermercado
coleccion = db.productos

filtro = {'nombre':'Cereal'}

try:
    modificacion = coleccion.delete_one(filtro)
    print('accion realizada')
except Exception as e:
    print(e)