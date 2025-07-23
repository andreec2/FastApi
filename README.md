
# FastAPI App

Este proyecto es una aplicación web construida con [FastAPI](https://fastapi.tiangolo.com/), un framework moderno y rápido para crear APIs con Python.

## Características

- API RESTful rápida y eficiente
- Soporte para documentación automática con Swagger y Redoc
- Fácil de extender y mantener

## Requisitos

- Python 3.8 o superior
- FastAPI
- Uvicorn

## Instalación

```bash
git clone https://github.com/andreec2/FastApi.git
cd fastapi-app
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn app.main:app --reload
```

Accede a la documentación automática en [http://localhost:8000/docs](http://localhost:8000/docs).

## Estructura del proyecto

fastapi-app/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── Config.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── session.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   └── __init__.py
├── main.py
├── requirements.txt
└── README.md


A continuación se explica el propósito de cada uno de los directorios y archivos principales del proyecto:

---

### `app/`
Paquete principal de la aplicación. Aquí se organizan todos los componentes, como rutas, lógica de negocio, base de datos y modelos.

---

### `app/api/`
Contiene los routers, es decir, los controladores o puntos de entrada HTTP (endpoints).  
Ejemplo: definición de rutas como `GET /users`, `POST /login`, etc.

- `routes.py`: define los endpoints usando FastAPI.

---

### `app/core/`
Incluye la configuración central del proyecto.

- `Config.py`: gestiona variables de entorno, claves secretas y configuraciones generales, normalmente usando `pydantic.BaseSettings`.

---

### `app/db/`
Responsable de la conexión y manejo de la base de datos.

- `session.py`: configura el motor y la sesión de la base de datos (por ejemplo, SQLAlchemy).

---

### `app/models/`
Define los modelos de datos, representando entidades del dominio.

- `user.py`: contiene clases que representan tablas de la base de datos o modelos de validación con Pydantic.

---

### `app/services/`
Incluye la lógica de negocio o reglas del dominio.

- `user_service.py`: funciones como `create_user`, `update_user`, `delete_user`, etc.

---

### `main.py`
Punto de entrada de la aplicación.  
Aquí se importa FastAPI, se montan los routers, se configuran middlewares y se ejecuta la app.

---

### `requirements.txt`
Lista de dependencias necesarias para ejecutar la aplicación.

---

### `README.md`
Documentación general del proyecto: instalación


## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.