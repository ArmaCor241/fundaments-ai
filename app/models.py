from app import db

class Herramienta(db.Model):
    __tablename__ = "herramientas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Herramienta {self.nombre}>"