# TravelSense — Agent.md: Listado de Requisitos

## 1. Descripción General del Sistema

**TravelSense** es una aplicación web de planificación de viajes que permite a los usuarios descubrir destinos turísticos, explorar eventos por ciudad y gestionar itinerarios personalizados.

La aplicación se estructura en dos capas:
- **Backend:** API REST con Python/Flask + base de datos SQLite.
- **Frontend:** Interfaz web en HTML/CSS/JavaScript que consume la API.

---

## 2. Requisitos Funcionales

### RF-01 — Gestión de Usuarios
| ID | Requisito |
|---|---|
| RF-01.1 | El sistema debe permitir listar todos los usuarios registrados. |
| RF-01.2 | El sistema debe permitir crear un nuevo usuario con nombre, email y preferencias. |
| RF-01.3 | Cada usuario tiene un identificador único autogenerado. |

### RF-02 — Gestión de Destinos
| ID | Requisito |
|---|---|
| RF-02.1 | El sistema debe ofrecer un catálogo de destinos turísticos agrupados por región y país. |
| RF-02.2 | Cada destino incluye: nombre, descripción, clima, país y región. |
| RF-02.3 | El sistema debe permitir listar todos los destinos disponibles. |

### RF-03 — Gestión de Eventos
| ID | Requisito |
|---|---|
| RF-03.1 | El sistema debe listar eventos culturales, deportivos y gastronómicos por destino. |
| RF-03.2 | Cada evento incluye: nombre, tipo, precio y el destino al que pertenece. |
| RF-03.3 | Los eventos deven poder filtrarse por destino. |

### RF-04 — Gestión de Itinerarios
| ID | Requisito |
|---|---|
| RF-04.1 | El sistema debe permitir crear itinerarios asociados a un usuario y un destino. |
| RF-04.2 | Cada itinerario incluye: fecha de inicio, fecha de fin, presupuesto y lista de actividades. |
| RF-04.3 | El sistema debe permitir listar todos los itinerarios con sus actividades asociadas. |

### RF-05 — Generación de Datos de Prueba
| ID | Requisito |
|---|---|
| RF-05.1 | El sistema debe poder generar datos falsos realistas (usuarios, destinos, eventos, itinerarios) mediante un script de setup. |
| RF-05.2 | Debe existir un endpoint `/api/v1/populate` que regenere la base de datos bajo demanda. |

---

## 3. Requisitos No Funcionales

| ID | Requisito |
|---|---|
| RNF-01 | La API debe responder en formato JSON. |
| RNF-02 | La API debe soportar CORS para permitir consumo desde el frontend. |
| RNF-03 | El sistema debe funcionar en local sin necesidad de conexión a internet. |
| RNF-04 | La base de datos debe ser SQLite (sin servidor externo requerido). |
| RNF-05 | El proyecto debe ser instalable con un único comando (`pip install -r requirements.txt`). |
| RNF-06 | El código debe estar versionado en un repositorio Git público. |

---

## 4. Actores del Sistema

| Actor | Descripción |
|---|---|
| **Usuario Viajero** | Consulta destinos, eventos y gestiona sus itinerarios. |
| **Administrador** | Regenera la base de datos y gestiona los datos del sistema. |

---

## 5. Casos de Uso Principales

```
[Usuario Viajero]
  --> CU-01: Explorar destinos por región
  --> CU-02: Ver eventos de un destino
  --> CU-03: Crear un itinerario personalizado
  --> CU-04: Ver mis itinerarios

[Administrador]
  --> CU-05: Regenerar base de datos con datos de prueba
```

---

## 6. Restricciones y Asunciones

- El sistema funciona únicamente en modo local (localhost:5000) durante el Sprint 2.
- No se implementa autenticación de usuarios en esta fase.
- Los datos de destinos y eventos se generan mediante la librería `Faker` y tablas precargadas.
