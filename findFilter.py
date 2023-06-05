from coneccion import *


db = client.Supermercado

# codigo = input("ingrese el codigo del producto")

coleccion = db.productos
documentos = coleccion.find({"ODOO UNI":"708000000"})

for documentos in documentos:
    print(documentos)

# ya no funciona!!!