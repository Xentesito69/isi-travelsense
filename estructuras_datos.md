# TravelSense — Interfaces y Estructuras de Datos

## 1. Modelo de Base de Datos (SQLite)

### Tabla `Usuarios`
| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER PK AUTOINCREMENT | Identificador único |
| `nombre` | TEXT | Nombre del usuario |
| `email` | TEXT | Correo electrónico |
| `preferencias` | TEXT | Preferencias de viaje (JSON/texto libre) |

### Tabla `Destinos`
| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER PK AUTOINCREMENT | Identificador único |
| `nombre` | TEXT | Nombre de la ciudad |
| `descripcion` | TEXT | Descripción breve del destino |
| `clima` | TEXT | Tipo de clima |
| `pais` | TEXT | País al que pertenece |
| `region` | TEXT | Región geográfica (Europa, América, etc.) |

### Tabla `Eventos`
| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER PK AUTOINCREMENT | Identificador único |
| `nombre` | TEXT | Nombre del evento |
| `tipo` | TEXT | Categoría (Música, Deporte, Cultura, etc.) |
| `precio` | TEXT | Precio de entrada |
| `destino_id` | INTEGER FK → Destinos.id | Destino al que pertenece |

### Tabla `Itinerarios`
| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER PK AUTOINCREMENT | Identificador único |
| `usuario_id` | INTEGER FK → Usuarios.id | Usuario dueño del itinerario |
| `destino_id` | INTEGER FK → Destinos.id | Destino del viaje |
| `fecha_inicio` | TEXT | Fecha de inicio del viaje |
| `fecha_fin` | TEXT | Fecha de fin del viaje |
| `presupuesto` | REAL | Presupuesto asignado (€) |

### Tabla `Actividades`
| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER PK AUTOINCREMENT | Identificador único |
| `itinerario_id` | INTEGER FK → Itinerarios.id | Itinerario al que pertenece |
| `nombre` | TEXT | Nombre de la actividad |
| `descripcion` | TEXT | Descripción de la actividad |
| `coste` | REAL | Coste estimado (€) |

---

## 2. Diagrama Entidad-Relación

```
┌──────────────┐       ┌──────────────────┐       ┌──────────────┐
│  Usuarios    │       │   Itinerarios    │       │   Destinos   │
│──────────────│       │──────────────────│       │──────────────│
│ id (PK)      │──1:N──│ id (PK)          │──N:1──│ id (PK)      │
│ nombre       │       │ usuario_id (FK)  │       │ nombre       │
│ email        │       │ destino_id (FK)  │       │ descripcion  │
│ preferencias │       │ fecha_inicio     │       │ clima        │
└──────────────┘       │ fecha_fin        │       │ pais         │
                       │ presupuesto      │       │ region       │
                       └────────┬─────────┘       └──────┬───────┘
                                │ 1:N                    │ 1:N
                       ┌────────▼─────────┐      ┌───────▼──────┐
                       │   Actividades    │      │   Eventos    │
                       │──────────────────│      │──────────────│
                       │ id (PK)          │      │ id (PK)      │
                       │ itinerario_id(FK)│      │ nombre       │
                       │ nombre           │      │ tipo         │
                       │ descripcion      │      │ precio       │
                       │ coste            │      │ destino_id   │
                       └──────────────────┘      └──────────────┘
```

---

## 3. Interfaz API REST — Contratos JSON

### GET `/api/v1/users`
**Response 200:**
```json
[
  {
    "id": 1,
    "nombre": "María García",
    "email": "m.garcia@email.com",
    "preferencias": "playa, gastronomía"
  }
]
```

### POST `/api/v1/users`
**Request Body:**
```json
{
  "nombre": "Juan López",
  "email": "j.lopez@email.com",
  "preferencias": "montaña, cultura"
}
```
**Response 201:**
```json
{ "id": 101, "nombre": "Juan López" }
```

### GET `/api/v1/destinations`
**Response 200:**
```json
[
  {
    "id": 5,
    "nombre": "Barcelona",
    "descripcion": "Arquitectura modernista y costa mediterránea",
    "clima": "Húmedo y suave",
    "pais": "España",
    "region": "Europa"
  }
]
```

### GET `/api/v1/events`
**Response 200:**
```json
[
  {
    "id": 12,
    "nombre": "Festival Primavera Sound",
    "tipo": "Música",
    "precio": "180€",
    "destino_id": 5,
    "destino_nombre": "Barcelona"
  }
]
```

### GET `/api/v1/itineraries`
**Response 200:**
```json
[
  {
    "id": 1,
    "usuario_id": 3,
    "usuario_nombre": "María García",
    "destino_id": 5,
    "destino_nombre": "Barcelona",
    "fecha_inicio": "2025-07-01",
    "fecha_fin": "2025-07-07",
    "presupuesto": 1200.0,
    "actividades": [
      {
        "id": 1,
        "itinerario_id": 1,
        "nombre": "Visita Sagrada Familia",
        "descripcion": "Tour guiado",
        "coste": 25.0
      }
    ]
  }
]
```

### POST `/api/v1/populate`
**Response 200:**
```json
{ "message": "Base de datos TravelSense poblada exitosamente." }
```

---

## 4. Estructuras de Datos Internas (Python)

### Pool de Destinos (`datos_viaje.py`)
```python
# Estructura del diccionario de destinos
lugares = {
    "Europa": {
        "España": [
            ("Madrid", "Capital cultural, museos y vida nocturna", "Variable"),
            # (nombre, descripcion, clima)
        ]
    }
}

# Lista plana resultante
DESTINOS_POOL = [
    # (nombre, descripcion, clima, pais, region)
    ("Madrid", "Capital cultural...", "Variable", "España", "Europa"),
]
```

### Eventos Genéricos
```python
GENERIC_EVENTS = [
    # (nombre_evento, tipo, precio)
    ('Mercado Local Artesanal', 'Cultura', 'Gratis'),
    ('Festival de Música Indie', 'Música', '30€'),
]
```
