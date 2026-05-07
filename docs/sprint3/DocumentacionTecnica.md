# Documentación Técnica — TravelSense

**Proyecto:** TravelSense — Plataforma inteligente de planificación de viajes  
**Versión:** Sprint 3 · Mayo 2026  
**Repositorio:** https://github.com/Xentesito69/isi-travelsense  
**Equipo:** Xentesito69 · noeliaasanchezc · Mariam770ts  
**Asignatura:** Ingeniería de Sistemas de Información (ISI)

---

## Índice

1. [Visión general del sistema](#1-visión-general-del-sistema)
2. [Arquitectura de la aplicación](#2-arquitectura-de-la-aplicación)
3. [Stack tecnológico](#3-stack-tecnológico)
4. [Estructura del repositorio](#4-estructura-del-repositorio)
5. [Backend — API REST](#5-backend--api-rest)
6. [Base de datos](#6-base-de-datos)
7. [Frontend](#7-frontend)
8. [Integraciones externas](#8-integraciones-externas)
9. [Despliegue](#9-despliegue)
10. [Tests automatizados](#10-tests-automatizados)
11. [Variables de entorno](#11-variables-de-entorno)
12. [Decisiones de diseño y limitaciones conocidas](#12-decisiones-de-diseño-y-limitaciones-conocidas)

---

## 1. Visión general del sistema

TravelSense es una plataforma web de planificación de viajes que combina:

- Un **catálogo de destinos globales** con información de clima y región.
- **Itinerarios personalizados** con actividades sugeridas y narración generada.
- Un **chat de asistente IA** impulsado por el modelo Gemini 2.0 Flash de Google.
- **Autenticación segura** mediante Google OAuth 2.0.
- Una **comunidad de viajeros** con sistema de seguimiento entre usuarios.

El sistema sigue una arquitectura cliente-servidor clásica desacoplada: el frontend es una SPA (Single Page Application) estática que consume una API REST en el backend.

---

## 2. Arquitectura de la aplicación

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENTE (Navegador)                       │
│                                                                  │
│   index.html + coords.js  (HTML / CSS / JavaScript vanilla)     │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP / HTTPS
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    NGINX (puerto 80)                             │
│                                                                  │
│   • Sirve los archivos estáticos del frontend                   │
│   • Proxy inverso: redirige /api/* al backend                   │
└────────────────────────────┬────────────────────────────────────┘
                             │ http://backend:5000
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│               FLASK + GUNICORN (puerto 5000)                    │
│                                                                  │
│   • API REST (versión v1)                                       │
│   • Lógica de autenticación Google OAuth                        │
│   • Integración con Gemini AI                                   │
│   • Acceso a la base de datos SQLite                            │
└──────────────┬──────────────────────────┬───────────────────────┘
               │                          │
               ▼                          ▼
┌──────────────────────┐     ┌─────────────────────────────────────┐
│   SQLite (archivo    │     │   APIs Externas                      │
│   travelsense.db)    │     │                                      │
│                      │     │  • Google OAuth 2.0 (autenticación) │
│   • Usuarios         │     │  • Google Gemini 2.0 Flash (IA)     │
│   • Destinos         │     └─────────────────────────────────────┘
│   • Itinerarios      │
│   • Actividades      │
│   • Eventos          │
└──────────────────────┘
```

### Flujo de una petición típica

1. El navegador carga `index.html` desde Nginx (puerto 80).
2. El JavaScript del frontend realiza peticiones `fetch()` a `/api/v1/*`.
3. Nginx intercepta las rutas `/api/*` y las redirige al backend Flask en el puerto 5000.
4. Flask procesa la petición, consulta SQLite y devuelve JSON.
5. El frontend renderiza los datos dinámicamente en el DOM.

---

## 3. Stack tecnológico

### Backend

| Componente | Tecnología | Versión |
|---|---|---|
| Lenguaje | Python | 3.11 |
| Framework web | Flask | 3.x |
| Servidor WSGI | Gunicorn | 26.x |
| CORS | Flask-CORS | 6.x |
| Base de datos | SQLite | (built-in Python) |
| Autenticación | google-auth | 2.x |
| IA generativa | google-genai | 1.x |
| Variables de entorno | python-dotenv | 1.x |
| Datos de prueba | Faker | 40.x |

### Frontend

| Componente | Tecnología |
|---|---|
| Estructura | HTML5 semántico |
| Estilos | CSS3 (vanilla, sin frameworks) |
| Lógica | JavaScript ES6+ (sin frameworks) |
| Servidor en producción | Nginx 1.25 Alpine |
| Autenticación | Google Identity Services (GSI) |

### Infraestructura

| Componente | Tecnología |
|---|---|
| Contenedores | Docker 29.x |
| Orquestación local | Docker Compose v2 |
| Orquestación producción | Kubernetes (manifiestos en `k8s/`) |
| Imagen base backend | python:3.11-slim |
| Imagen base frontend | nginx:1.25-alpine |

### Testing

| Componente | Tecnología |
|---|---|
| Framework de tests | pytest 9.x |
| Cliente HTTP para tests | requests |

---

## 4. Estructura del repositorio

```
isi-travelsense/
│
├── backend/
│   ├── app.py               # Aplicación Flask principal, definición de rutas
│   ├── setup_database.py    # Creación de tablas y generación de datos de prueba
│   ├── database.py          # Helper de conexión a SQLite
│   ├── datos_viaje.py       # Pool de datos: destinos, eventos, templates
│   ├── generador.py         # Lógica auxiliar de generación de itinerarios
│   ├── requirements.txt     # Dependencias Python
│   ├── Dockerfile           # Imagen Docker del backend (multi-stage)
│   ├── entrypoint.sh        # Script de inicio: init BD + arranque gunicorn
│   ├── .env.example         # Plantilla de variables de entorno
│   └── README.md
│
├── frontend/
│   ├── index.html           # SPA completa (HTML + CSS + JS en un único archivo)
│   ├── coords.js            # Coordenadas geográficas para el mapa
│   ├── logo.png             # Logotipo versión clara
│   ├── logodark.png         # Logotipo versión oscura
│   ├── Dockerfile           # Imagen Docker del frontend (Nginx)
│   └── nginx.conf           # Configuración de Nginx (proxy + SPA fallback)
│
├── k8s/
│   ├── namespace.yaml       # Namespace "travelsense" en Kubernetes
│   ├── secret.yaml          # Secretos de API (plantilla, rellenar con valores reales)
│   ├── backend-pvc.yaml     # PersistentVolumeClaim para SQLite
│   ├── backend-deployment.yaml  # Deployment + Service del backend (2 réplicas)
│   ├── frontend-deployment.yaml # Deployment + Service del frontend (2 réplicas)
│   └── ingress.yaml         # Ingress con enrutamiento /api/* → backend
│
├── docs/
│   ├── sprint1/             # Documentación del Sprint 1
│   ├── sprint2/             # Documentación del Sprint 2
│   ├── sprint3/             # Documentación del Sprint 3 (este documento)
│   └── ComoEntrarATravelSense.md  # Guía de despliegue rápido
│
├── tests/
│   ├── test_suite.py        # 25 tests de integración con pytest
│   ├── test_api.py          # Tests legacy (script independiente)
│   ├── ComoEjecutarLosTest.md  # Guía de ejecución de tests
│   └── README.md
│
├── docker-compose.yml       # Orquestación local de los dos contenedores
├── start.bat                # Script de arranque local sin Docker (Windows)
├── .gitignore               # Exclusiones de control de versiones
└── README.md                # Descripción general del proyecto
```

---

## 5. Backend — API REST

### Base URL

```
http://localhost:5000/api/v1
```

En producción con Docker/Nginx, el frontend accede vía proxy en:

```
http://localhost/api/v1
```

### Endpoints

#### `POST /auth/google`

Autentica un usuario mediante un token de Google OAuth 2.0.

**Request body:**
```json
{
  "credential": "<JWT token de Google Identity Services>"
}
```

**Respuesta exitosa (200):**
```json
{
  "id": 42,
  "google_id": "1234567890",
  "nombre": "Juan García",
  "email": "juan@gmail.com",
  "preferencias": "Cultura, Gastronomía",
  "historial_viajes": null,
  "pais": null
}
```

**Lógica:**
1. Verifica el JWT con `google.oauth2.id_token.verify_oauth2_token()`.
2. Tolera hasta 30 segundos de desviación de reloj (NTP drift).
3. Si el usuario ya existe por `google_id` → devuelve sus datos.
4. Si existe por `email` pero sin `google_id` → vincula el ID y devuelve.
5. Si es nuevo → inserta en `Usuarios` y devuelve el registro creado.

**Errores:**
| Código | Causa |
|---|---|
| `400` | Falta el campo `credential` en el body |
| `401` | Token inválido o expirado |

---

#### `POST /chat`

Envía una pregunta al asistente IA (Gemini 2.0 Flash).

**Request body:**
```json
{
  "pregunta": "¿Qué ropa debo llevar a Tokio en enero?"
}
```

**Respuesta exitosa (200):**
```json
{
  "respuesta": "En enero, Tokio puede ser bastante frío (entre 2°C y 10°C). Te recomiendo llevar..."
}
```

**Prompt del sistema:** `"Eres el asistente de la empresa TravelSense. Responde en el mismo idioma en que te hablen."`

**Modo fallback:** Si no hay API key configurada, devuelve una respuesta placeholder sin llamar a Gemini.

**Errores:**
| Código | Causa |
|---|---|
| `400` | Falta el campo `pregunta` |
| `500` | Error en la API de Gemini (ej. cuota agotada) |

---

#### `GET /users`

Devuelve todos los usuarios registrados.

**Respuesta (200):**
```json
[
  {
    "id": 1,
    "google_id": "abc123",
    "nombre": "Javier García",
    "email": "javier@travelsense.com",
    "preferencias": "Gastronomía, Cultura",
    "historial_viajes": null,
    "pais": "España"
  }
]
```

---

#### `POST /users`

Crea un nuevo usuario manualmente.

**Request body:**
```json
{
  "nombre": "María López",
  "email": "maria@ejemplo.com",
  "preferencias": "Naturaleza, Aventura"
}
```

**Respuesta (201):**
```json
{
  "id": 105,
  "nombre": "María López"
}
```

**Errores:**
| Código | Causa |
|---|---|
| `400` | Falta el campo `nombre` |

---

#### `GET /destinations`

Devuelve todos los destinos disponibles en la plataforma.

**Respuesta (200):**
```json
[
  {
    "id": 1,
    "nombre": "Tokio",
    "descripcion": "La capital de Japón, metrópoli futurista...",
    "clima_tipico": "Templado",
    "pais": "Japón",
    "region": "Asia"
  }
]
```

---

#### `GET /events`

Devuelve todos los eventos disponibles con el nombre del destino asociado (JOIN).

**Respuesta (200):**
```json
[
  {
    "id": 1,
    "destino_id": 1,
    "nombre": "Festival de los Cerezos en Flor",
    "tipo": "Cultural",
    "fecha": "2026-06-15",
    "precio": "Gratuito",
    "destino_nombre": "Tokio"
  }
]
```

---

#### `GET /itineraries`

Devuelve todos los itinerarios con sus actividades y los nombres del usuario y destino (JOINs).

**Respuesta (200):**
```json
[
  {
    "id": 1,
    "usuario_id": 3,
    "destino_id": 1,
    "fecha": "2026-06-20",
    "resumen_narrativo": "¡Javier! Tu aventura en Tokio está lista...",
    "clima_actual": "Soleado",
    "usuario_nombre": "Javier García",
    "destino_nombre": "Tokio",
    "actividades": [
      {
        "id": 1,
        "itinerario_id": 1,
        "nombre": "Visita guiada: Lo mejor de Tokio",
        "tipo": "General",
        "hora": "09:30",
        "justificacion_ia": "Coincide con tus intereses culturales."
      }
    ]
  }
]
```

---

#### `POST /populate`

Vacía y repobla la base de datos con datos de ejemplo.

> ⚠️ Elimina todos los datos existentes antes de insertar.

**Respuesta (200):**
```json
{
  "message": "Base de datos TravelSense poblada exitosamente."
}
```

Genera:
- **100 usuarios** con nombres internacionales aleatorios
- **Todos los destinos** del pool global (fichero `datos_viaje.py`)
- **100 itinerarios** con 3 actividades cada uno
- **Eventos locales** para cada destino

---

## 6. Base de datos

TravelSense utiliza **SQLite** como motor de base de datos. El fichero se almacena en `travelsense.db` (o en la ruta indicada por la variable `DB_PATH` en entornos Docker).

### Diagrama Entidad-Relación

```
┌─────────────────────┐         ┌─────────────────────────────┐
│      Usuarios       │         │          Destinos            │
│─────────────────────│         │─────────────────────────────│
│ id (PK)            │         │ id (PK)                     │
│ google_id (UNIQUE) │         │ nombre                      │
│ nombre             │         │ descripcion                 │
│ email (UNIQUE)     │         │ clima_tipico                │
│ preferencias       │         │ pais                        │
│ historial_viajes   │         │ region                      │
│ pais               │         └──────────────┬──────────────┘
└──────────┬──────────┘                        │
           │                                   │
           │ 1                             1   │
           ▼ N                             N   ▼
┌──────────────────────────────────────────────────────────────┐
│                        Itinerarios                           │
│──────────────────────────────────────────────────────────────│
│ id (PK)                                                      │
│ usuario_id (FK → Usuarios.id)                               │
│ destino_id (FK → Destinos.id)                               │
│ fecha (TEXT, formato YYYY-MM-DD)                            │
│ resumen_narrativo                                           │
│ clima_actual                                                │
└──────────────────────────────┬───────────────────────────────┘
                               │ 1
                               ▼ N
                ┌──────────────────────────────┐
                │         Actividades           │
                │──────────────────────────────│
                │ id (PK)                      │
                │ itinerario_id (FK)           │
                │ nombre                       │
                │ tipo                         │
                │ hora (HH:MM)                │
                │ justificacion_ia             │
                └──────────────────────────────┘

┌─────────────────────────────────────────────┐
│                   Eventos                    │
│─────────────────────────────────────────────│
│ id (PK)                                     │
│ destino_id (FK → Destinos.id)              │
│ nombre                                      │
│ tipo                                        │
│ fecha (TEXT, formato YYYY-MM-DD)           │
│ precio                                      │
└─────────────────────────────────────────────┘
```

### Notas sobre el modelo de datos

- **SQLite** no tiene tipos estrictos: las fechas se almacenan como `TEXT` en formato `YYYY-MM-DD`.
- Los campos `preferencias` e `historial_viajes` de `Usuarios` son cadenas de texto libre (no arrays normalizados), lo que facilita la lectura y escritura pero limita consultas complejas.
- En entorno Docker, la BD se monta en un volumen (`db_data`) para garantizar persistencia entre reinicios del contenedor.
- El endpoint `POST /populate` recrea todas las tablas desde cero; no existe migraciones incrementales.

---

## 7. Frontend

El frontend es una **Single Page Application (SPA)** implementada íntegramente en un único fichero `index.html` (~330 KB) que contiene HTML, CSS y JavaScript.

### Secciones de la aplicación

| Sección | ID del panel | Descripción |
|---|---|---|
| Dashboard | `home` | Vista principal con estadísticas, pasaporte virtual y destinos visitados |
| Destinos | `destinations` | Catálogo filtrable de destinos con búsqueda |
| Eventos | `events` | Eventos locales por destino |
| Itinerarios | `itineraries` | Creación y visualización de itinerarios con actividades |
| Asistente IA | `chat` | Chat conversacional con Gemini |
| Viajeros | `travelers` | Comunidad de usuarios, sistema de seguimiento (follow/unfollow) |
| Perfil | `profile` | Gestión de datos personales, avatar, preferencias |
| Configuración | `settings` | Preferencias de la cuenta, privacidad |

### Gestión del estado

Al ser vanilla JavaScript sin framework, el estado se gestiona mediante:

- **`localStorage`**: persistencia de sesión del usuario (datos de Google Auth, preferencias, destinos visitados, listas de seguidos/seguidores).
- **`sessionStorage`**: datos temporales de sesión.
- **Variables globales en módulo**: estado de la UI activa (panel seleccionado, filtros aplicados).

### Comunicación con el backend

Todas las llamadas al backend se realizan con la API `fetch()` nativa:

```javascript
// Ejemplo: cargar destinos
const response = await fetch('/api/v1/destinations');
const destinations = await response.json();
```

El prefijo `/api/v1/` es interceptado por Nginx en el contenedor de producción y redirigido al backend Flask.

### Sistema de autenticación en el cliente

Se utiliza la librería oficial de **Google Identity Services (GSI)**:

```html
<script src="https://accounts.google.com/gsi/client" async defer></script>
```

El token JWT generado por Google se envía al backend para verificación:

```javascript
google.accounts.id.initialize({
  client_id: GOOGLE_CLIENT_ID,
  callback: async ({ credential }) => {
    const res = await fetch('/api/v1/auth/google', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ credential })
    });
    const user = await res.json();
    // Guardar usuario en localStorage
  }
});
```

---

## 8. Integraciones externas

### Google OAuth 2.0

| Parámetro | Valor |
|---|---|
| Librería cliente | Google Identity Services (GSI) |
| Librería servidor | `google-auth` (Python) |
| Variable de entorno | `GOOGLE_CLIENT_ID` |
| Flujo | Implicit Flow (token JWT) |
| Tolerancia de reloj | 30 segundos (NTP drift) |

El Client ID de Google se configura en el fichero `.env` de la raíz y se pasa al contenedor Docker vía `docker-compose.yml`.

### Google Gemini 2.0 Flash

| Parámetro | Valor |
|---|---|
| SDK | `google-genai` 1.x (nuevo SDK oficial) |
| Modelo | `gemini-2.0-flash` |
| Variable de entorno | `GEMINI_API_KEY` |
| Endpoint usado | `client.models.generate_content()` |
| Modo fallback | Respuesta placeholder si no hay API key |

> **Nota:** La librería `google-generativeai` está deprecada. TravelSense usa el nuevo SDK `google-genai` que es el recomendado actualmente por Google.

---

## 9. Despliegue

### Modo 1 — Docker Compose (recomendado)

Levanta automáticamente el frontend (Nginx) y el backend (Flask + Gunicorn) en contenedores aislados.

```bash
# Primer arranque (construye las imágenes):
docker compose up --build -d

# Arranques posteriores (sin reconstruir):
docker compose up -d

# Ver estado:
docker compose ps

# Ver logs:
docker compose logs -f

# Parar:
docker compose down
```

**Puertos expuestos:**

| Servicio | Puerto |
|---|---|
| Frontend (Nginx) | 80 → http://localhost |
| Backend (Flask) | 5000 → http://localhost:5000 |

**Volúmenes:**

| Volumen | Ruta en contenedor | Propósito |
|---|---|---|
| `db_data` | `/app/data/travelsense.db` | Persistencia de la base de datos SQLite |

**Inicialización automática de la BD:** El script `entrypoint.sh` comprueba si el fichero de BD existe; si no, ejecuta `setup_database.py` para crear las tablas y poblarlas con datos de ejemplo antes de arrancar Gunicorn.

---

### Modo 2 — Kubernetes (producción)

Los manifiestos en `k8s/` permiten desplegar la aplicación en cualquier cluster Kubernetes.

```bash
# Aplicar todos los manifiestos:
kubectl apply -f k8s/

# Verificar pods:
kubectl get pods -n travelsense

# Ver servicios:
kubectl get services -n travelsense
```

**Manifiestos incluidos:**

| Fichero | Recurso K8s | Descripción |
|---|---|---|
| `namespace.yaml` | Namespace | Aísla todos los recursos bajo `travelsense` |
| `secret.yaml` | Secret | Credenciales de API (rellenar antes de aplicar) |
| `backend-pvc.yaml` | PersistentVolumeClaim | 1 Gi para la BD SQLite |
| `backend-deployment.yaml` | Deployment + Service | 2 réplicas del backend, ClusterIP |
| `frontend-deployment.yaml` | Deployment + Service | 2 réplicas del frontend, ClusterIP |
| `ingress.yaml` | Ingress | Enrutamiento público `/api/*` → backend, `/` → frontend |

**Estrategia de despliegue:** `RollingUpdate` con `maxUnavailable: 0` garantiza zero-downtime en actualizaciones.

---

### Modo 3 — Local sin Docker

Para desarrollo sin contenedores en Windows:

```bash
.\start.bat
```

El script instala las dependencias, inicializa la BD y arranca Flask en modo debug en `http://localhost:5000`. En este modo el frontend se sirve como archivo estático local.

---

## 10. Tests automatizados

### Localización

```
tests/test_suite.py
```

### Ejecución

```bash
# Instalar dependencias de test:
py -m pip install pytest requests

# Con el servidor corriendo (Docker o local):
py -m pytest tests/test_suite.py -v
```

### Cobertura de tests

| Clase | Tests | Endpoints cubiertos |
|---|---|---|
| `TestDestinations` | 5 | `GET /destinations` |
| `TestUsers` | 7 | `GET /users`, `POST /users` |
| `TestEvents` | 5 | `GET /events` |
| `TestItineraries` | 5 | `GET /itineraries` |
| `TestPopulate` | 3 | `POST /populate` |
| **Total** | **25** | **5 endpoints** |

Los tests verifican: códigos HTTP, tipos de respuesta, integridad de campos, JOINs entre tablas, validación de errores (400) y formato de datos.

---

## 11. Variables de entorno

| Variable | Obligatoria | Descripción |
|---|---|---|
| `GOOGLE_CLIENT_ID` | Sí (para auth real) | Client ID del proyecto de Google Cloud |
| `GEMINI_API_KEY` | Sí (para IA real) | Clave de API de Google AI Studio |
| `DB_PATH` | No | Ruta completa al fichero SQLite. Por defecto: `travelsense.db` en el directorio de trabajo |

**Ficheros de configuración:**

| Fichero | Uso |
|---|---|
| `.env` (raíz) | Variables para `docker-compose.yml` |
| `backend/.env` | Variables para ejecución local sin Docker |
| `backend/.env.example` | Plantilla con valores de ejemplo |
| `k8s/secret.yaml` | Variables para Kubernetes (valores en base64) |

---

## 12. Decisiones de diseño y limitaciones conocidas

### Decisiones tomadas

| Decisión | Justificación |
|---|---|
| SQLite en lugar de PostgreSQL | Reduce la complejidad de infraestructura para un proyecto académico; sin necesidad de un servicio de BD separado |
| SPA en un solo fichero HTML | Elimina la necesidad de un bundler (Webpack/Vite) y simplifica el despliegue |
| Vanilla JS sin framework | Demuestra dominio de los fundamentos web; reduce dependencias |
| Multi-stage Dockerfile | Separa la instalación de dependencias del runtime, reduciendo el tamaño de la imagen final |
| Gunicorn como servidor WSGI | Flask dev server no es apto para producción; Gunicorn gestiona múltiples workers |
| `google-genai` (nuevo SDK) | La librería `google-generativeai` fue deprecada en 2025; migración proactiva al SDK actual |

### Limitaciones conocidas

| Limitación | Impacto | Mitigación posible |
|---|---|---|
| SQLite con `ReadWriteOnce` | No escala horizontalmente (un solo writer) | Migrar a PostgreSQL para producción real |
| Sin sistema de migraciones | `POST /populate` borra todos los datos | Implementar Alembic o migraciones manuales |
| JWT almacenado en localStorage | Vulnerable a XSS | Mover a cookies `HttpOnly` en producción |
| API key de Gemini con límite de cuota gratuita | El chat puede devolver 429 | Upgrade del plan o implementar caché de respuestas |
| Sin paginación en los endpoints GET | Puede ser lento con muchos datos | Añadir parámetros `limit` y `offset` |

---

*Documentación técnica — Sprint 3 — ISI 2025/26*
