from flask import current_app as app, render_template, request, redirect, url_for
from app import db
from app.models import Herramienta

# Ruta principal: Ver el catálogo de herramientas
@app.route("/")
def index():
    herramientas = Herramienta.query.order_by(Herramienta.id.desc()).all()
    return render_template("index.html", herramientas=herramientas)

# Ruta para agregar herramientas manualmente
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")

        if nombre and descripcion:
            nueva_herramienta = Herramienta(
                nombre=nombre.strip(),
                descripcion=descripcion.strip()
            )
            db.session.add(nueva_herramienta)
            db.session.commit()
            return redirect(url_for("index"))

    return render_template("agregar.html")