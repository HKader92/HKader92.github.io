import db
from sqlalchemy import Column, Integer, String, Boolean


class Proveedor(db.Base):
    __tablename__= "proveedor"
    id = Column(Integer, primary_key=True)
    empresa = Column(String(200), nullable=False)
    direccion = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    telefono = Column(Integer, nullable=False)
    CIF = Column(String(9), nullable=False)
    hecho = Column(Boolean)
    def __init__(self, empresa, direccion, email, telefono, CIF, hecho):

        self.empresa = empresa
        self.telefono = telefono
        self.direccion = direccion
        self.CIF = CIF
        self.email = email
        self.hecho = hecho

    def __repr__(self):
        return "Proveedor {}: {} {} {} {} {} ({})".format(self.id, self.empresa, self.direccion,
                                                          self.email, self.telefono, self.CIF,
                                                          self.hecho)

    def __str__(self):
        return  "Proveedor {}: {} {} {} {} {} ({})".format(self.id, self.empresa, self.direccion,
                                                          self.email, self.telefono, self.CIF,
                                                          self.hecho)

class Producto(db.Base):
    __tablename__="productos"
    id = Column(Integer, primary_key=True)
    marca = Column(String(200), nullable=False)
    modelo = Column(String(200), nullable=False)
    discrepcion = Column(String(400), nullable=False)


    def __init__(self, marca, modelo, discrepcion, hecho):

        self.marca = marca
        self.modelo = modelo
        self.discrepcion = discrepcion
        self.hecho = hecho

    def __repr__(self):
        return "Producto {}: {} {} {} ({})".format(self.id, self.marca, self.modelo, self.discrepcion, self.hecho)

    def __str__(self):
        return "Producto {}: {} {} {} ({})".format(self.id, self.marca, self.modelo, self.discrepcion, self.hecho)