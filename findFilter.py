from coneccion import *

codigo = input("ingrese el codigo del producto")
db.cliente.Supermercado
coleccion = db.productos
documentos = coleccion.find({"nombre":"Cereal"})

for documentos in documentos:
    print(documentos)