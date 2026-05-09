<div align="center">

![TravelSense Logo](TravelSenceLogo.png)

# TravelSense

### Plataforma inteligente de planificación de viajes

[![ISI](https://img.shields.io/badge/Asignatura-ISI%202025--2026-blue)](https://github.com/Xentesito69/isi-travelsense)
[![Python](https://img.shields.io/badge/Python-3.11-green)](https://python.org)
[![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey)](https://flask.palletsprojects.com)
[![Docker](https://img.shields.io/badge/Deploy-Docker%20%2F%20Kubernetes-informational)](https://docker.com)

</div>

---

## 📌 Descripción general

**TravelSense** es una plataforma web de planificación de viajes que combina un catálogo global de destinos, generación de itinerarios personalizados, un asistente IA conversacional y una comunidad de viajeros. El sistema sigue una arquitectura cliente–servidor desacoplada: el frontend es una SPA estática que consume una API REST del backend.

---

## 👥 Equipo y roles

| Nombre | GitHub | Rol |
|---|---|---|
| Vicente | [@Xentesito69](https://github.com/Xentesito69) | DevOps / Testing (Docker, K8s, CI, tests automatizados) |
| Noelia | [@noeliaasanchezc](https://github.com/noeliaasanchezc) | Backend / Integración (API REST, lógica de negocio, BD) |
| Mariam | [@Mariam770ts](https://github.com/Mariam770ts) | Frontend / UX (SPA, diseño, flujos de usuario) |

---

## 🧩 Funcionalidades principales

- 🌍 **Catálogo de destinos** — más de 250 destinos globales con clima y región
- 🗓️ **Itinerarios personalizados** — actividades organizadas por día con resumen narrativo generado
- 🤖 **Asistente IA** — chat conversacional impulsado por **Google Gemini 2.0 Flash**
- 🔐 **Autenticación segura** — inicio de sesión con **Google OAuth 2.0** (Google Identity Services)
- 📅 **Eventos locales** — eventos culturales y de ocio por destino
- 👥 **Comunidad de viajeros** — sistema de seguimiento (follow/unfollow) entre usuarios
- 👤 **Perfil de usuario** — avatar, preferencias, pasaporte virtual y destinos visitados
- 📦 **Despliegue containerizado** — Docker Compose para local y Kubernetes para producción

---

## 🏗️ Arquitectura

```
┌──────────────────────────────────────────────────────────────┐
│                    CLIENTE (Navegador)                        │
│        index.html + coords.js  (HTML / CSS / JS vanilla)     │
└────────────────────────────┬─────────────────────────────────┘
                             │ HTTP / HTTPS
                             ▼
┌──────────────────────────────────────────────────────────────┐
│                    NGINX (puerto 80)                          │
│  • Sirve archivos estáticos del frontend                     │
│  • Proxy inverso: redirige /api/* → backend                  │
└────────────────────────────┬─────────────────────────────────┘
                             │ http://backend:5000
                             ▼
┌──────────────────────────────────────────────────────────────┐
│              FLASK + GUNICORN (puerto 5000)                   │
│  • API REST v1                                               │
│  • Autenticación Google OAuth                                │
│  • Integración con Gemini AI                                 │
└──────────────┬──────────────────────────┬────────────────────┘
               │                          │
               ▼                          ▼
┌──────────────────────┐     ┌─────────────────────────────────┐
│   SQLite             │     │   APIs Externas                  │
│   (travelsense.db)   │     │  • Google OAuth 2.0             │
│                      │     │  • Google Gemini 2.0 Flash      │
│  • Usuarios          │     └─────────────────────────────────┘
│  • Destinos          │
│  • Itinerarios       │
│  • Actividades       │
│  • Eventos           │
└──────────────────────┘
```

---

## 🛠️ Stack tecnológico

### Backend
| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.11 |
| Framework | Flask 3.x + Gunicorn |
| Base de datos | SQLite (built-in) |
| Autenticación | `google-auth` 2.x |
| IA generativa | `google-genai` 1.x (Gemini 2.0 Flash) |
| Variables de entorno | `python-dotenv` |

### Frontend
| Componente | Tecnología |
|---|---|
| Estructura | HTML5 semántico |
| Estilos | CSS3 vanilla |
| Lógica | JavaScript ES6+ (sin frameworks) |
| Servidor | Nginx 1.25 Alpine |
| Autenticación | Google Identity Services (GSI) |

### Infraestructura
| Componente | Tecnología |
|---|---|
| Contenedores | Docker 29.x |
| Orquestación local | Docker Compose v2 |
| Orquestación producción | Kubernetes (manifiestos en `k8s/`) |

---

## 📂 Estructura del repositorio

```
TravelSense/
│
├── backend/
│   ├── app.py               # API Flask — definición de todos los endpoints
│   ├── database.py          # Helper de conexión a SQLite
│   ├── setup_database.py    # Crea tablas e inserta datos de prueba
│   ├── datos_viaje.py       # Pool de ~250 destinos y eventos
│   ├── generador.py         # Lógica de generación de itinerarios
│   ├── requirements.txt     # Dependencias Python
│   ├── Dockerfile           # Imagen Docker del backend (multi-stage)
│   ├── entrypoint.sh        # Init BD + arranque Gunicorn
│   └── .env.example         # Plantilla de variables de entorno
│
├── frontend/
│   ├── index.html           # SPA completa (HTML + CSS + JS)
│   ├── coords.js            # Coordenadas geográficas para el mapa
│   ├── logo.png / logodark.png
│   ├── Dockerfile           # Imagen Docker del frontend (Nginx)
│   └── nginx.conf           # Configuración Nginx (proxy + SPA fallback)
│
├── k8s/
│   ├── namespace.yaml
│   ├── secret.yaml
│   ├── backend-pvc.yaml
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   └── ingress.yaml
│
├── docs/
│   ├── sprint1/             # Modelo de negocio, análisis de mercado, OKRs
│   ├── sprint2/             # Arquitectura, stack tecnológico, mockups UX
│   ├── sprint3/             # Documentación técnica completa + Manual de usuario
│   └── ComoEntrarATravelSense.md
│
├── tests/
│   ├── test_suite.py        # 25 tests de integración con pytest
│   ├── test_api.py          # Tests adicionales
│   └── ComoEjecutarLosTest.md
│
├── docker-compose.yml       # Orquestación local (frontend + backend)
├── start.bat                # Arranque local sin Docker (Windows)
├── .gitignore
└── README.md
```

---

## 🚀 Despliegue

### Opción 1 — Docker Compose *(recomendado)*

```bash
# Variables de entorno necesarias en .env (raíz):
# GOOGLE_CLIENT_ID=...
# GEMINI_API_KEY=...

# Primer arranque (construye las imágenes):
docker compose up --build -d

# Arranques posteriores:
docker compose up -d

# Ver logs:
docker compose logs -f

# Parar:
docker compose down
```

| Servicio | URL |
|---|---|
| Frontend | http://localhost |
| Backend API | http://localhost:5000/api/v1 |

> La base de datos se inicializa automáticamente en el primer arranque vía `entrypoint.sh`.

---

### Opción 2 — Kubernetes *(producción)*

```bash
kubectl apply -f k8s/
kubectl get pods -n travelsense
```

Estrategia `RollingUpdate` con `maxUnavailable: 0` → **zero-downtime deployments**.

---

### Opción 3 — Local sin Docker *(Windows)*

```bash
# Copiar backend/.env.example → backend/.env y rellenar las claves
.\start.bat
```

Arranca Flask en modo debug en `http://localhost:5000`.

---

## 🔌 API REST

Base URL: `http://localhost:5000/api/v1`

| Método | Ruta | Descripción |
|---|---|---|
| `POST` | `/auth/google` | Autenticación SSO con Google |
| `POST` | `/chat` | Chat con el asistente Gemini IA |
| `GET` | `/users` | Lista de usuarios |
| `POST` | `/users` | Crear usuario |
| `GET` | `/destinations` | Catálogo de destinos |
| `GET` | `/events` | Eventos por destino |
| `GET` | `/itineraries` | Itinerarios con actividades |
| `POST` | `/populate` | Repoblar BD con datos de prueba |

---

## 🧪 Tests

25 tests de integración con `pytest` que cubren todos los endpoints principales.

```bash
# Con el servidor en marcha:
py -m pytest tests/test_suite.py -v
```

Ver [`tests/ComoEjecutarLosTest.md`](tests/ComoEjecutarLosTest.md) para instrucciones detalladas.

---

## 🔑 Variables de entorno

| Variable | Descripción |
|---|---|
| `GOOGLE_CLIENT_ID` | Client ID de Google Cloud (para autenticación) |
| `GEMINI_API_KEY` | Clave de Google AI Studio (para el asistente IA) |
| `DB_PATH` | Ruta al fichero SQLite (opcional; por defecto `travelsense.db`) |

---

## 📄 Documentación

| Documento | Descripción |
|---|---|
| [`docs/sprint3/DocumentacionTecnica.md`](docs/sprint3/DocumentacionTecnica.md) | Documentación técnica completa del sistema |
| [`docs/sprint3/ManualDeUsuario.md`](docs/sprint3/ManualDeUsuario.md) | Manual de usuario con guías paso a paso |
| [`docs/ComoEntrarATravelSense.md`](docs/ComoEntrarATravelSense.md) | Guía rápida de despliegue |

---

*Proyecto académico — Ingeniería de Sistemas de Información (ISI) · 2025/26*
