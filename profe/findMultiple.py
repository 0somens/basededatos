from conectar import *


def conectar():
    db = cliente.profesorDataBase
    coleccion = db.Productos
    documentos = coleccion.find()

    for documentos in documentos:
        return(documentos)