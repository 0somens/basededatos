from profe.conectar import *
db = cliente.profesorDataBase
coleccion = db.Productos
filtro = {"SAP":"12096549"}
update = {"$set":{"CATEG NESTLÉ":"Galletas","CATEG NESTLÉ":"Galletitas de niños"}}

try:
    modificar = coleccion.update_one(filtro,update)
    print("Actualizacion Realizada")
except Exception as e:
    print (e)
