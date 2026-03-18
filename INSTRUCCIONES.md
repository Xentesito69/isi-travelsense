# 🧳 Setup de TravelSense

Aquí tienes la **secuencia exacta** para correr el proyecto en otro ordenador desde cero, sin errores.

## 1. Requisitos Previos
El otro ordenador necesita tener **Python** instalado. 
Si no lo tiene, que lo descargue de [python.org](https://www.python.org/downloads/) (Importante: Marcar la casilla "Add Python to PATH" al instalar).

## 2. Instalación (Solo la primera vez)
Abre la terminal (Símbolo del sistema o PowerShell) en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará `Flask` y `Faker` automáticamente.

## 3. Generar la Base de Datos
Para que la web tenga datos (usuarios, viajes, destinos), ejecuta este comando:

```bash
python setup_database.py
```
*(Verás mensajes confirmando que se han creado 100 usuarios y 100 itinerarios).*

## 4. Ejecutar la Web
Para arrancar el servidor:

```bash
python app.py
```

Verás un mensaje diciendo `Running on http://127.0.0.1:5000`.

## 5. Abrir la Web
Abre tu navegador (Chrome, Edge, etc.) y entra en:
👉 `http://127.0.0.1:5000`

---
**Nota:** Si al ejecutar `python` da error, prueba con `py` en su lugar (ej: `py app.py`).
