from flask import Flask, render_template, request, redirect
from coneccion import conexion
from bson import ObjectId


app = Flask(__name__)

@app.route('/')
def home():
    db = conexion()
    Clientes = db.Clientes
    datos = Clientes.find()

    Pedidos = db.Pedidos
    datospedidos = Pedidos.find()

    Menús = db.Menús
    datosmenus = Menús.find()

    return render_template('index.html', Clientes=datos, Pedidos=datospedidos, Menús=datosmenus)



# CLIENTES ADMINISTRACION
@app.route('/insertar_cliente', methods=['POST'])
def insertar_cliente():
    db = conexion()
    Clientes = db.Clientes

    name = request.form['name']
    apellido = request.form['apellido']
    phone = request.form['phone']
    address = request.form['address']
    mail = request.form['mail']

    cliente = {
        'name': name,
        'apellido': apellido,
        'phone': phone,
        'address': address,
        'mail': mail
    }
    
    Clientes.insert_one(cliente)

    return redirect('/')        
@app.route('/actualizar-cliente', methods=['POST'])
def actualizar_cliente():
    # Obtén los datos enviados desde el formulario
    cliente_id = request.form['id_cliente']
    name = request.form['name_cliente']
    apellido = request.form['apellido_cliente']
    phone = request.form['phone_cliente']
    address = request.form['address_cliente']
    mail = request.form['mail_cliente']
    # Realiza la actualización en la base de datos
    db = conexion()
    Clientes = db.Clientes

    Clientes.update_one(
        {'_id': ObjectId(cliente_id)},
        {"$set": {
            'name': name,
            'apellido': apellido,
            'phone': phone,
            'address': address,
            'mail': mail,
            'estado': 1
        }}
    )

    # Redirecciona a la página principal u otra página de éxito
    return redirect('/')






# PEDIDO ADMINISTRACION
@app.route('/insertar_pedido', methods=['POST'])
def insertar_pedido():
    db = conexion()
    Pedidos = db.Pedidos

    cliente = request.form['Cliente']
    fecha = request.form['Fecha']
    nombre_plato = request.form['Plato1']
    cantidad = request.form['Cantidad']
    precio_unitario = request.form['PrecioUnitario']

    pedido = {
        "Cliente": cliente,
        "Fecha": fecha,
        "Artículos": [
            {
                "Nombre": nombre_plato,
                "Cantidad": cantidad,
                "PrecioUnitario": precio_unitario
            }
        ]
    }
    Pedidos.insert_one(pedido)
    # Aquí puedes insertar el pedido en la base de datos MongoDB

    return redirect('/') 





# MENU ADMINISTRACION
@app.route('/insertar_menu', methods=['POST'])
def insertar_menu():
    db = conexion()
    Menús = db.Menús

    nombre = request.form['NameMenu']
    descripcion = request.form['DescripcionMenu']

    plato1 = request.form['NombrePlato1']
    desc1 = request.form['DescripcionPlato1']
    price1 = request.form['PrecioPlato1']

    plato2 = request.form['NombrePlato2']
    desc2 = request.form['DescripcionPlato2']
    price2 = request.form['PrecioPlato2']

    platopos = request.form['NombrePostre']
    descpos = request.form['DescripcionPostre']
    pricepos = request.form['PrecioPostre']

    menu = {
        "Nombre": nombre,
        "Descripción": descripcion,
        "Platos": [
            {
                "Nombre": plato1,
                "Descripción": desc1,
                "Precio": price1
            },
            {
                "Nombre": plato2,
                "Descripción": desc2,
                "Precio": price2
            },
            {
                "Nombre": platopos,
                "Descripción": descpos,
                "Precio": pricepos
            }
        ]
    }

    Menús.insert_one(menu)
    # Aquí puedes insertar el menú en la base de datos MongoDB

    return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)
