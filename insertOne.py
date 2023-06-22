from coneccion import *
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Supermercado

coleccion = db.proveedores

nombre = "Matias Osores"
direccion = "psj x 321"
telefono = "+569 3456 4321"
correo_electronico = "matias.osores@inacapmail.cl"

documentos = {
	"nombre": "qwerrt",
	"direccion":"psj imaginario 123",
	"telefono": "+569 1234 4321",
	"correo_electronico":"mati.osores@gmail.com"
      } 
try:
	modificacion = coleccion.insert_one(documentos)
	print('accion realizada')
except Exception as e:
	print(e)