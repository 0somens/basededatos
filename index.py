from flask import *

from coneccion import *

app = Flask(__name__)

@app.route('/')

def home():
    db = conexion()
    lista = db.Lista
    datos = lista.find()

    return render_template #Esto manda a llamar a la /templates/index.html para que una vez cargado aparezca en pantalla 