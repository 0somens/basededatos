from flask import Flask, render_template, request, redirect
from coneccion import conexion
from bson import ObjectId


app = Flask(__name__)

@app.route('/')
def home():
    db = conexion()
    Clientes = db.Clientes
    datos = Clientes.find({"estado":1})

    Pedidos = db.Pedidos
    datospedidos = Pedidos.find({"estado":1})

    Menús = db.Menús
    datosmenus = Menús.find({"estado":1})

    return render_template('index.html', Clientes=datos, Pedidos=datospedidos, Menús=datosmenus)


# -------------------- SEARCHER -------------------- #
# -------------------- SEARCHER -------------------- #
# -------------------- SEARCHER -------------------- #

@app.route('/searcher', methods=['POST'])
def buscador():
    db = conexion()
    find = request.form['searcher']
    # PENDIENTE
    



# -------------------- SEARCHER -------------------- #
# -------------------- SEARCHER -------------------- #
# -------------------- SEARCHER -------------------- #





# -------------------- CLIENTES ADMINISTRACION -------------------- #
# -------------------- CLIENTES ADMINISTRACION -------------------- #
# -------------------- CLIENTES ADMINISTRACION -------------------- #
# -------------------- CLIENTES ADMINISTRACION -------------------- #
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
        'mail': mail,
        'estado': 1
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
    if 'Eliminar' in request.form:
        # Obtén el ID del cliente a "eliminar"
        cliente_id = request.form['Eliminar']
        Clientes.update_one({'_id': ObjectId(cliente_id)}, {"$set": {'estado': 0}})
        
        # Redirecciona a la página principal u otra página de éxito
        return redirect('/')
    else:
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


# Quizas ni siquiera se use esta funcion ya que al momento de actualizar un cliente podra elegir el boton 
# y en el caso de ser el boton eliminar se actualizaria el estado del cliente a 0
def eliminar_cliente():
    # Obtén los datos enviados desde el formulario
    cliente_id = request.form['id_cliente']
    # Elimina el cliente de la base de datos
    db = conexion()
    Clientes = db.Clientes
    Clientes.update_one(
        {'_id': ObjectId(cliente_id)},
        {"$set": {
            'estado': 0 
            }}
        )
    # Redirecciona a la página principal u otra página de éxito
    return redirect('/')









# -------------------- PEDIDO ADMINISTRACION -------------------- #
# -------------------- PEDIDO ADMINISTRACION -------------------- #
# -------------------- PEDIDO ADMINISTRACION -------------------- #
# -------------------- PEDIDO ADMINISTRACION -------------------- #
# -------------------- PEDIDO ADMINISTRACION -------------------- #
@app.route('/insertar_pedido', methods=['POST'])
def insertar_pedido():
    db = conexion()
    Pedidos = db.Pedidos
    Clientes = db.Clientes
    

    cliente = request.form['Cliente']
    if not Clientes.find_one({"_id": ObjectId(cliente)}):
        return "El _id del cliente no se ha encontrado"
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
        ],
        'estado': 1
    }
    Pedidos.insert_one(pedido)
    # Aquí puedes insertar el pedido en la base de datos MongoDB

    return redirect('/')
@app.route('/actualizar-pedido', methods=['POST'])
def actualizar_pedido():
    pedido_id = request.form['id_pedido']
    cliente_id = request.form['Cliente']
    fecha = request.form['Fecha']
    
    # Obtén los datos de los artículos
    articulos = []
    for i in range(1, 6):  # Suponiendo un máximo de 5 artículos por pedido
        nombre = request.form.get(f'Plato{i}', '')
        cantidad = int(request.form.get(f'Cantidad{i}', '0'))
        precio_unitario = float(request.form.get(f'PrecioUnitario{i}', '0.0'))
        if nombre:
            articulos.append({
                'Nombre': nombre,
                'Cantidad': cantidad,
                'PrecioUnitario': precio_unitario
            })

    # Realiza la actualización en la base de datos
    db = conexion()
    Pedidos = db.Pedidos
    if 'Eliminar' in request.form:
        pedido_id = request.form['Eliminar']
        Pedidos.update_one({'_id': ObjectId(pedido_id)}, {"$set": {'estado': 0}})
        return redirect('/')
    else:
        Pedidos.update_one(
            {'_id': ObjectId(pedido_id)},
            {"$set": {
                'Cliente': cliente_id,
                'Fecha': fecha,
                'Artículos': articulos,
                'estado': 1
            }}
        )
        return redirect('/')
#-------------------- MENU ADMINISTRACION --------------------#
#-------------------- MENU ADMINISTRACION --------------------#
#-------------------- MENU ADMINISTRACION --------------------#
#-------------------- MENU ADMINISTRACION --------------------#
#-------------------- MENU ADMINISTRACION --------------------#
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
        ],
        'estado': 1
    }

    Menús.insert_one(menu)
    # Aquí puedes insertar el menú en la base de datos MongoDB

    return redirect('/')

@app.route('/actualizar_menu', methods=['POST'])
def actualizar_menu():
    menu_id = request.form['id_menu']
    nombre_menu = request.form['NameMenu']
    descripcion_menu = request.form['DescripcionMenu']
    
    # Obtén los datos de los platos
    platos = []
    for i in range(1, 6):  # Suponiendo un máximo de 5 platos en el menú
        nombre_plato = request.form.get(f'NombrePlato{i}', '')
        descripcion_plato = request.form.get(f'DescripcionPlato{i}', '')
        precio_plato = float(request.form.get(f'PrecioPlato{i}', '0.0'))
        if nombre_plato:
            platos.append({
                'Nombre': nombre_plato,
                'Descripción': descripcion_plato,
                'Precio': precio_plato
            })

    # Realiza la actualización en la base de datos
    db = conexion()
    Menus = db.Menús
    if 'Eliminar' in request.form:
        menu_id = request.form['Eliminar']
        Menus.update_one({'_id': ObjectId(menu_id)}, {"$set": {'estado': 0}})
        return redirect('/')
    else:
        Menus.update_one(
            {'_id': ObjectId(menu_id)},
            {"$set": {
                'Nombre': nombre_menu,
                'Descripción': descripcion_menu,
                'Platos': platos,
                'estado': 1
            }}
        )
        return redirect('/')








if __name__ == '__main__':
    app.run(debug=True)
