from coneccion import *
from index import *


client = MongoClient(uri, server_api=ServerApi('1'))

db = client.get_database('restauranteDB')

coleccion = db.get_collection('Clientes')
# Get data from HTML form
nombre = request.form.get('name')
apellido = request.form.get('apellido')
telefono = request.form.get('telefono')
direccion = request.form.get('direccion')
mail = request.form.get('email')


documentos = {
	"name": nombre,
	"apellido": apellido,
	"phone": telefono,
	"address": direccion,
	"email": mail
      } 
try:
	modificacion = coleccion.insert_one(documentos)
	print('accion realizada')
except Exception as e:
	print(e)
 