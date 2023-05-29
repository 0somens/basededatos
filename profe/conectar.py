from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://ptaipe:plto4956@inacap2023.guvc7ax.mongodb.net/?retryWrites=true&w=majority"

#Crear un nuevo cliente de conexion remota
cliente = MongoClient(uri, server_api=ServerApi('1'))
try:
    cliente.admin.command('ping')
    print("Conexion Exitosa con Atlas. (Y)")
    
except Exception as e:
    print(e)