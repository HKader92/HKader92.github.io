from flask import Flask, render_template, request, redirect, url_for
import db
from models import Proveedor, Producto

app = Flask(__name__)




@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/add-producto', methods=['POST'])
def crearProducto():
    producto = Producto(marca=request.form['marca'],
                        modelo=request.form['modelo'],
                        discrepcion=request.form['discrepcion'],
                        hecho=False)
    db.session.add(producto)
    db.session.commit()
   # return 'guardado'

    todos_los_productos = db.session.query(Producto).all()
    return render_template("productos.html", lista_de_productos=todos_los_productos)

@app.route('/eliminar-producto/<id>')
def eliminarProducto(id):
    producto = db.session.query(Producto).filter_by(id=int(id)).delete()
    db.session.commit()
    return render_template('productos.html')

@app.route('/producto-hecho/<id>')
def productoHecho(id):
    producto = db.session.query(Producto).filter_by(id=int(id)).first()
    producto.hecho = not(producto.hecho)
    db.session.commit()
    return redirect(url_for('productos.html'))


@app.route('/productos')
def producto():
    return render_template('productos.html')




@app.route('/add-proveedor', methods=['POST'])
def crear():
    proveedor = Proveedor(empresa=request.form['empresa'],
                          direccion=request.form['direccion'],
                          email=request.form['email'],
                          telefono=request.form['phone'],
                          CIF=request.form['CIF'],
                          hecho=False)
    db.session.add(proveedor)
    db.session.commit()
    # return 'guardado'

    todos_los_proveedores = db.session.query(Proveedor).all()
    return render_template("proveedores.html", lista_de_proveedores=todos_los_proveedores)

@app.route('/eliminar-proveedor/<id>')
def eliminar(id):
    proveedor = db.session.query(Proveedor).filter_by(id=int(id)).delete()
    db.session.commit()
    return render_template('proveedores.html')

@app.route('/proveedor-hecho/<id>')
def hecho(id):
    proveedor = db.session.query(Proveedor).filter_by(id=int(id)).first()
    proveedor.hecho = not(proveedor.hecho)
    db.session.commit()
    return redirect(url_for('proveedor'))

@app.route('/proveedores')
def proveedor():
    return render_template('proveedores.html')







@app.route('/asesoramiento')
def asesoramiento():
    return render_template('asesoramiento.html')




if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)