# 🚀 Cómo Ejecutar y Acceder a TravelSense

**Proyecto:** TravelSense — Plataforma inteligente de planificación de viajes  
**Repositorio:** https://github.com/Xentesito69/isi-travelsense  
**Equipo:** Xentesito69 · noeliaasanchezc · Mariam770ts

---

## Requisitos previos

| Herramienta | Versión mínima | Descarga |
|---|---|---|
| **Docker Desktop** | 24.x o superior | https://www.docker.com/products/docker-desktop |
| **Git** | cualquiera | https://git-scm.com |

> No se necesita instalar Python, Node.js ni ninguna otra dependencia. Docker lo gestiona todo.

---

## Pasos para ejecutar la aplicación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Xentesito69/isi-travelsense.git
cd isi-travelsense
```

### 2. Asegurarse de que Docker Desktop está abierto

Abre **Docker Desktop** desde el menú de inicio de Windows y espera a que el icono de la ballena aparezca en la barra de tareas sin animación (indica que está listo).

### 3. Levantar la aplicación

Desde la carpeta raíz del proyecto, ejecuta:

```bash
docker compose up --build -d
```

> La primera vez tardará 2-3 minutos mientras descarga las imágenes base y las dependencias. Las siguientes veces será casi instantáneo gracias a la caché de Docker.

### 4. Acceder a la aplicación

Una vez completado el paso anterior, abre el navegador y entra en:

```
http://localhost
```

✅ La aplicación estará disponible. No hace falta ninguna configuración adicional.

---

## Qué ocurre internamente

```
Navegador (puerto 80)
       │
       ▼
 ┌─────────────┐
 │   Nginx     │  ← sirve el frontend (HTML/CSS/JS)
 │  Frontend   │
 └──────┬──────┘
        │  /api/* → proxy
        ▼
 ┌─────────────┐
 │    Flask    │  ← API REST (puerto 5000)
 │   Backend   │
 └──────┬──────┘
        │
        ▼
 ┌─────────────┐
 │   SQLite    │  ← base de datos persistente (volumen Docker)
 └─────────────┘
```

- El **frontend** (Nginx) recibe todo el tráfico en el puerto 80.
- Las peticiones a rutas `/api/*` se redirigen automáticamente al backend Flask.
- La base de datos SQLite se inicializa automáticamente con datos de ejemplo en el primer arranque.

---

## Endpoints de la API REST

| Método | Ruta | Descripción |
|---|---|---|
| `POST` | `/api/v1/auth/google` | Autenticación con Google OAuth |
| `GET` | `/api/v1/destinations` | Lista de destinos disponibles |
| `GET` | `/api/v1/events` | Eventos por destino |
| `GET` | `/api/v1/itineraries` | Itinerarios guardados |
| `GET` | `/api/v1/users` | Usuarios registrados |
| `POST` | `/api/v1/chat` | Chat con el asistente IA (Gemini) |
| `POST` | `/api/v1/populate` | Repoblar la BD con datos de ejemplo |

Para explorar la API directamente: `http://localhost:5000/api/v1/destinations`

---

## Funcionalidades principales de la app

Una vez dentro de `http://localhost`, el profesor puede explorar:

| Sección | Descripción |
|---|---|
| 🏠 **Dashboard** | Vista principal con estadísticas y el pasaporte virtual |
| 🗺️ **Destinos** | Catálogo de destinos con filtros |
| 📅 **Eventos** | Eventos disponibles por destino |
| 🗒️ **Itinerarios** | Creación y gestión de itinerarios de viaje |
| 🤖 **Asistente IA** | Chat con Gemini para recomendaciones de viaje |
| 👤 **Perfil** | Gestión de cuenta y preferencias |
| 👥 **Viajeros** | Comunidad de usuarios, sistema de seguimiento |

> El acceso requiere iniciar sesión con una cuenta de Google.

---

## Comandos de gestión

```bash
# Ver el estado de los contenedores
docker compose ps

# Ver los logs en tiempo real
docker compose logs -f

# Parar la aplicación (conserva los datos)
docker compose down

# Parar y eliminar todos los datos (reinicio limpio)
docker compose down -v

# Volver a arrancar sin reconstruir las imágenes
docker compose up -d
```

---

## Modo alternativo: ejecución local sin Docker

Si Docker no está disponible, la aplicación también puede ejecutarse directamente:

```bash
# Windows — doble clic en start.bat, o desde PowerShell:
.\start.bat
```

Este script instala las dependencias de Python, inicializa la base de datos y arranca el servidor Flask en `http://localhost:5000`. En este modo el frontend se abre directamente como archivo HTML local.

**Requisito:** Python 3.10 o superior instalado en el sistema.

---

## Credenciales y variables de entorno

Las claves de API necesarias (Google OAuth y Gemini) ya están preconfiguradas en el fichero `.env` de la raíz del proyecto para facilitar la evaluación.

> ⚠️ En un entorno de producción real estas claves se gestionarían mediante secretos cifrados (Kubernetes Secrets / Sealed Secrets).

---

## Despliegue en Kubernetes (producción)

Los manifiestos para despliegue automático en un cluster Kubernetes están disponibles en la carpeta `k8s/`:

```
k8s/
├── namespace.yaml          # Namespace aislado "travelsense"
├── secret.yaml             # Secretos de API (rellenar con valores reales)
├── backend-pvc.yaml        # Volumen persistente para SQLite
├── backend-deployment.yaml # Deployment + Service del backend (2 réplicas)
├── frontend-deployment.yaml# Deployment + Service del frontend (2 réplicas)
└── ingress.yaml            # Ingress con enrutamiento /api/* → backend
```

Para aplicar todos los manifiestos:

```bash
kubectl apply -f k8s/
```

---

*Documentación generada para evaluación académica — Sprint 2 — ISI 2025/26*
