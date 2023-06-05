from flask import *

from coneccion import *

app = Flask(__name__)

@app.route('/')

def home():
    db = conexion()
    lista = db.proveedores
    datos = lista.find()

    return render_template('index.html', lista = datos) #Esto manda a llamar a la /templates/index.html para que una vez cargado aparezca en pantalla 
if __name__ == '__main__':
    app.run(debug=True) #Ejecuta la aplicacion del Main en modo de prueba (mientras el servidor este activo puedo modificar y puedo ver lo cambios de manera sincronica )