from conectar import *
db = cliente.profesorDataBase
coleccion = db.Productos

categoria = input("ingrese una categoria a su producto: ")
ODOOUNI = input("ingrese nuevo codigo ODOO UNI: ")
Uni_venta = input("Ingrese nueva unidad de venta: ")
UnidadMedida = input("Ingrese nueva unidad de medida: ")
EANUNIVTA = input("Ingrese nueva EANUNIVTA: ")
SAP = input("Ingrese nuevo codigo SAP: ")
DESCRIPCION = input("Ingrese nueva descripcion: ")
PrecioNeto = input("Ingrese precio neto: ")
PrecioBruto =  input("Ingrese ingrese precio bruto: ")

nuevo_documentos = {"CATEG NESTLÉ":categoria,"ODOO UNI":ODOOUNI,"Unidad de venta":Uni_venta,
                    "Unidad de medida":UnidadMedida,"EAN UNI VTA":EANUNIVTA,"SAP":SAP,"DESCRIPCIÓN SKU":DESCRIPCION,
                    "Precio neto":PrecioNeto,"Precio bruto":PrecioBruto
                    }

resultado = coleccion.insert_one(nuevo_documentos)

print("El codigo del nuevo producto es: ",resultado.inserted_id)