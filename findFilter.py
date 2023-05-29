from coneccion import *

db = client.Supermercado

# codigo = input("ingrese el codigo del producto")

coleccion = db.productos
documentos = coleccion.find({"nombre":"Cereal"})

for documentos in documentos:
    print(documentos)