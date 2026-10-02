import os
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuración de la Base de Datos
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "herramientas")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()


class Herramienta(Base):
    __tablename__ = "herramientas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=False)


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


def guardar_herramientas():
    try:
        engine = create_engine(DATABASE_URL, echo=False)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        print("Conectado a la BD 'herramientas'. Insertando registros...")

        for item in herramientas_trabajo:
            nueva_herramienta = Herramienta(
                nombre=item["nombre"], descripcion=item["descripcion"]
            )
            session.add(nueva_herramienta)

        session.commit()
        print(
            f"¡Éxito! Se guardaron {len(herramientas_trabajo)} herramientas en la base de datos 'herramientas'."
        )

    except Exception as e:
        print(f"Error durante la ejecución: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    guardar_herramientas()