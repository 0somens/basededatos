from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://matiasosores:XJLMzLTVcFYc7iCt@tienda.ietwuqs.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
def conexion():
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Coneccion exitosa")
        db = client.Productos1
        return db
    except Exception as e:
        print(e)
conexion()
# Ahora funciona