# TravelSense — Tecnologías Utilizadas

## Stack Tecnológico

### Backend

| Tecnología | Versión | Rol |
|---|---|---|
| **Python** | 3.10+ | Lenguaje principal del servidor |
| **Flask** | Latest | Framework web ligero para la API REST |
| **Flask-CORS** | Latest | Permite peticiones cross-origin desde el frontend |
| **SQLite** | Integrado en Python | Base de datos relacional sin servidor |
| **Faker** | Latest | Generación de datos de prueba realistas |

### Frontend

| Tecnología | Versión | Rol |
|---|---|---|
| **HTML5** | — | Estructura de la interfaz web |
| **CSS3** | — | Estilos y diseño visual |
| **JavaScript (Vanilla)** | ES6+ | Lógica del cliente y llamadas a la API |

### Herramientas de Desarrollo

| Herramienta | Uso |
|---|---|
| **Git + GitHub** | Control de versiones y repositorio remoto |
| **VS Code** | Editor principal |
| **diagrams.net** | Diagramas de arquitectura |
| **Postman / curl** | Testing manual de la API REST |
| **pip** | Gestión de dependencias Python |

---

## Justificación de Elecciones

### ¿Por qué Flask?
Flask es un microframework Python ideal para prototipos y proyectos académicos. Permite crear una API REST completa con pocas líneas de código, sin la complejidad de Django. Su ecosistema es sencillo: basta con `app.py` para tener el servidor funcionando.

### ¿Por qué SQLite?
SQLite no requiere servidor de base de datos separado — el archivo `.db` se genera localmente. Perfecto para desarrollo local y entornos de clase donde no se puede instalar PostgreSQL o MySQL.

### ¿Por qué Faker?
Faker genera datos sintéticos realistas (nombres, emails, fechas, etc.) que permiten poblar la base de datos con 100 usuarios e itinerarios de forma automatizada, sin tener que introducir datos manualmente.

### ¿Por qué HTML/CSS/JS puro?
Para el Sprint 2 la interfaz se desarrolla en HTML puro sin frameworks (React, Vue...) para mantener la simplicidad del proyecto y poder prototiparlo rápidamente.

---

## Diagrama de Dependencias

```
Frontend (HTML/JS)
      │
      │ HTTP (fetch API)
      ▼
Backend (Flask - Python)
      │
      │ sqlite3 module
      ▼
Base de Datos (SQLite - travelsense.db)
```

---

## Instalación y Ejecución

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Generar la base de datos
python setup_database.py

# 3. Arrancar el servidor
python app.py
# → Disponible en http://127.0.0.1:5000
```
