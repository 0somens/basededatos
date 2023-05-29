from conectar import *

db = cliente.profesorDataBase
coleccion = db.Productos

#codigo = input("Ingrese codigo SAP: ")"05052023235"  SAP: '12096549'"_id":ObjectId(codigo)

documentos = coleccion.find({"SAP":"12096549"})

for documentos in documentos:
    print(documentos)