import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instancia global de SQLAlchemy
db = SQLAlchemy()


def seed_db():
    from app.models import Herramienta

    # Verifica si la tabla herramientas ya contiene registros
    if Herramienta.query.first() is None:
        herramientas_trabajo = [
            {
                "nombre": "Martillo",
                "descripcion": "Herramienta manual de percusión compuesta por una cabeza pesada y un mango, diseñada para golpear, clavar, moldear o romper diferentes materiales.",
            },
            {
                "nombre": "Destornillador",
                "descripcion": "Herramienta manual utilizada para apretar o aflojar tornillos aplicando torque mediante la punta ajustada a la ranura de la cabeza del tornillo.",
            },
            {
                "nombre": "Alicate",
                "descripcion": "Pinza de metal articulada con brazos forjados que se utiliza para sujetar, doblar o cortar cables, alambres y piezas pequeñas.",
            },
            {
                "nombre": "Llave ajustable",
                "descripcion": "Herramienta de mano con una mordaza móvil que se adapta a diferentes medidas de tuercas y pernos para apretarlos o aflojarlos.",
            },
            {
                "nombre": "Cincel",
                "descripcion": "Herramienta de corte manual con boca acerada y recta que sirve para labrar, cortar o ranurar piedra, concreto o metales mediante golpes de martillo.",
            },
            {
                "nombre": "Sierra de mano",
                "descripcion": "Herramienta compuesta por una hoja dentada de acero sujeto a un mango, diseñada para cortar madera o materiales blandos mediante vaivén.",
            },
            {
                "nombre": "Flexómetro",
                "descripcion": "Cinta métrica enrollable construida en chapa de acero graduada en centímetros y pulgadas, alojada en una caja protectora para medir longitudes.",
            },
            {
                "nombre": "Nivel de gota",
                "descripcion": "Instrumento de medición utilizado para verificar la perfecta horizontalidad o verticalidad de una superficie mediante una burbuja dentro de un tubo con líquido.",
            },
            {
                "nombre": "Taladro",
                "descripcion": "Herramienta giratoria de perforación que hace rotar una broca a altas revoluciones para realizar agujeros en madera, metal, plástico o mampostería.",
            },
            {
                "nombre": "Esmeril angular",
                "descripcion": "Herramienta eléctrica portátil que utiliza discos abrasivos giratorios para cortar, desbastar o pulir metales, piedra y concreto.",
            },
            {
                "nombre": "Calibrador Vernier",
                "descripcion": "Instrumento de medición de alta precisión equipado con regleta y nonio para obtener lecturas exactas de diámetros exteriores, interiores y profundidades.",
            },
            {
                "nombre": "Cautín eléctrico",
                "descripcion": "Herramienta de trabajo con punta metálica calefactada que alcanza altas temperaturas para fundir estaño y realizar soldaduras en electrónica.",
            },
            {
                "nombre": "Maza",
                "descripcion": "Herramienta de percusión similar a un martillo pero con cabeza más grande y pesada, empleada en demolición y construcción pesada.",
            },
            {
                "nombre": "Prensa de banco",
                "descripcion": "Dispositivo mecánico de sujeción que se fija a la mesa de trabajo para inmovilizar piezas firmemente mientras se procesan.",
            },
            {
                "nombre": "Gato hidráulico",
                "descripcion": "Máquina impulsada por presión de fluido utilizada para elevar cargas pesadas, vehículos o estructuras con poco esfuerzo manual.",
            },
            {
                "nombre": "Pistola de calor",
                "descripcion": "Herramienta eléctrica que emite un flujo constante de aire caliente para decaparse pintura, moldear plásticos o contraer tubos termorretráctiles.",
            },
            {
                "nombre": "Pinza ponchadora RJ45",
                "descripcion": "Herramienta de prensado de terminales diseñada para fijar los conectores modulares de red a los extremos de cables de datos UTP.",
            },
            {
                "nombre": "Multímetro",
                "descripcion": "Instrumento eléctrico de medición que combina voltímetro, amperímetro y óhmetro para diagnosticar parámetros en circuitos eléctricos.",
            },
            {
                "nombre": "Lija de mano",
                "descripcion": "Soporte de papel o tela con granos de material abrasivo adheridos que se usa para alisar, pulir o limpiar superficies de madera y metal.",
            },
            {
                "nombre": "Cepillo de carpintero",
                "descripcion": "Herramienta de mano con cuchilla ajustable en la base utilizada para rebajar, emparejar y cepillar virutas de madera.",
            },
        ]

        print("Poblando la base de datos por primera vez...")
        for item in herramientas_trabajo:
            nueva_herramienta = Herramienta(
                nombre=item["nombre"], descripcion=item["descripcion"]
            )
            db.session.add(nueva_herramienta)

        db.session.commit()
        print("¡Base de datos poblada exitosamente!")


def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos PostgreSQL mediante variables de entorno
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "herramientas")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "clave_secreta_fundaments_ai"

    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)

    with app.app_context():
        from app import routes

        db.create_all()  # Crea las tablas si no existen
        seed_db()  # Puebla los datos si la tabla está vacía

    return app