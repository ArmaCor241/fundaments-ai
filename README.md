# Fundaments AI - Sistema de Gestión y Aprendizaje de Herramientas

Este proyecto es una aplicación web desarrollada en Python con **Flask** y **PostgreSQL** (gestionado con **SQLAlchemy** y desplegado en **Docker**). El objetivo principal del sistema es catalogar herramientas de trabajo, almacenar sus especificaciones y servir como base para la integración de un **Spider/Web Scraper** capaz de extraer información y permitir que el sistema "aprenda" y categorice nuevas herramientas de manera autónoma.

---

## Características Principales

* **Base de datos relacional:** Persistencia en PostgreSQL ejecutado mediante contenedores Docker.
* **Carga Inicial (Seeder):** Script automatizado para poblar la base de datos con 20 herramientas de trabajo fundamentales.
* **Interfaz Web (Flask):** Vista interactiva para consultar la lista de herramientas y formulario para registrar nuevas herramientas manualmente.
* **Módulo de Extracción Automática (Spider):** Integración para obtener descripciones y características de herramientas directamente desde la web.

---

## Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Framework Web:** Flask
* **ORM:** SQLAlchemy
* **Base de Datos:** PostgreSQL
* **Infraestructura:** Docker / Docker Desktop
* **Control de Versiones:** Git & GitHub

---

## Estructura del Proyecto

```text
fundaments-ai/
│
├── app/                     # Aplicación principal en Flask
│   ├── static/              # Archivos estáticos (CSS, JS, imágenes)
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   ├── templates/           # Plantillas HTML (Jinja2)
│   │   ├── base.html        # Plantilla base
│   │   ├── index.html       # Catálogo de herramientas
│   │   └── agregar.html     # Formulario de registro de herramientas
│   ├── __init__.py          # Inicialización de la aplicación e integración de la BD
│   ├── models.py            # Definición de modelos SQLAlchemy (Herramienta)
│   ├── routes.py            # Rutas y controladores de la aplicación
│   └── scraper.py           # Spider/Scraper para extracción de datos web
│
├── venv/                    # Entorno virtual de Python (Ignorado en Git)
├── cargar_herramientas.py   # Script de carga masiva inicial (Seeder)
├── run.py                   # Punto de entrada para ejecutar el servidor Flask
├── requirements.txt         # Dependencias del proyecto
├── .gitignore               # Exclusión de archivos y carpetas temporales
└── README.md                # Documentación del proyecto