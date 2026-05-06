# 🧪 Cómo Ejecutar los Tests de TravelSense

**Proyecto:** TravelSense — Suite de tests automatizados  
**Framework:** pytest · Tipo: tests de integración contra la API REST

---

## Requisitos

| Herramienta | Cómo instalar |
|---|---|
| **Python 3.10+** | https://www.python.org/downloads |
| **pytest** | `pip install pytest` |
| **requests** | `pip install requests` |

Instalación rápida de ambos:
```bash
pip install pytest requests
```

> Los tests son de **integración**: hablan con la API real, así que el servidor debe estar corriendo antes de ejecutarlos.

---

## Paso 1 — Arrancar el servidor

Elige **una** de estas dos opciones:

### Opción A · Con Docker (recomendada, sin instalar nada más)
```bash
docker compose up -d
```
El servidor quedará disponible en `http://localhost:5000`.

### Opción B · Con Python directamente
```bash
# Desde la raíz del proyecto:
python backend/app.py
```
O en Windows:
```bash
.\start.bat
```

Espera hasta ver:
```
* Running on http://0.0.0.0:5000
```

---

## Paso 2 — Ejecutar los tests

Desde la **raíz del proyecto**:

```bash
pytest tests/test_suite.py -v
```

La opción `-v` (verbose) muestra el nombre de cada test y su resultado individual.

### Salida esperada

```
tests/test_suite.py::TestDestinations::test_destinations_returns_200        PASSED
tests/test_suite.py::TestDestinations::test_destinations_returns_list       PASSED
tests/test_suite.py::TestDestinations::test_destinations_not_empty          PASSED
tests/test_suite.py::TestDestinations::test_destinations_have_required_fields PASSED
tests/test_suite.py::TestDestinations::test_destinations_nombre_not_empty   PASSED
tests/test_suite.py::TestUsers::test_users_returns_200                      PASSED
tests/test_suite.py::TestUsers::test_users_returns_list                     PASSED
tests/test_suite.py::TestUsers::test_users_have_required_fields             PASSED
tests/test_suite.py::TestUsers::test_create_user_returns_201                PASSED
tests/test_suite.py::TestUsers::test_create_user_returns_id                 PASSED
tests/test_suite.py::TestUsers::test_create_user_nombre_matches             PASSED
tests/test_suite.py::TestUsers::test_create_user_missing_nombre_returns_400 PASSED
tests/test_suite.py::TestEvents::test_events_returns_200                    PASSED
tests/test_suite.py::TestEvents::test_events_returns_list                   PASSED
tests/test_suite.py::TestEvents::test_events_not_empty                      PASSED
tests/test_suite.py::TestEvents::test_events_have_destino_nombre            PASSED
tests/test_suite.py::TestEvents::test_events_have_required_fields           PASSED
tests/test_suite.py::TestItineraries::test_itineraries_returns_200          PASSED
tests/test_suite.py::TestItineraries::test_itineraries_returns_list         PASSED
tests/test_suite.py::TestItineraries::test_itineraries_include_actividades  PASSED
tests/test_suite.py::TestItineraries::test_itineraries_include_user_and_dest_names PASSED
tests/test_suite.py::TestItineraries::test_itineraries_fecha_format         PASSED
tests/test_suite.py::TestPopulate::test_populate_returns_200                PASSED
tests/test_suite.py::TestPopulate::test_destinations_exist_after_populate   PASSED
tests/test_suite.py::TestPopulate::test_users_exist_after_populate          PASSED

========================= 25 passed in X.XXs =========================
```

---

## Qué prueba cada grupo de tests

### 🗺️ `TestDestinations` — Destinos (5 tests)
| Test | Qué verifica |
|---|---|
| `test_destinations_returns_200` | El endpoint responde con HTTP 200 |
| `test_destinations_returns_list` | La respuesta es una lista JSON |
| `test_destinations_not_empty` | La BD tiene al menos 1 destino |
| `test_destinations_have_required_fields` | Cada destino tiene `id`, `nombre`, `pais`, `region` |
| `test_destinations_nombre_not_empty` | Ningún destino tiene nombre vacío |

### 👤 `TestUsers` — Usuarios (7 tests)
| Test | Qué verifica |
|---|---|
| `test_users_returns_200` | El endpoint responde con HTTP 200 |
| `test_users_returns_list` | La respuesta es una lista JSON |
| `test_users_have_required_fields` | Cada usuario tiene `id`, `nombre`, `email` |
| `test_create_user_returns_201` | Crear un usuario devuelve HTTP 201 |
| `test_create_user_returns_id` | El usuario creado tiene un `id` numérico |
| `test_create_user_nombre_matches` | El nombre guardado coincide con el enviado |
| `test_create_user_missing_nombre_returns_400` | Sin `nombre` devuelve HTTP 400 |

### 📅 `TestEvents` — Eventos (5 tests)
| Test | Qué verifica |
|---|---|
| `test_events_returns_200` | El endpoint responde con HTTP 200 |
| `test_events_returns_list` | La respuesta es una lista JSON |
| `test_events_not_empty` | La BD tiene al menos 1 evento |
| `test_events_have_destino_nombre` | El JOIN con Destinos funciona correctamente |
| `test_events_have_required_fields` | Cada evento tiene `id`, `nombre`, `tipo`, `fecha`, `precio` |

### 🗒️ `TestItineraries` — Itinerarios (5 tests)
| Test | Qué verifica |
|---|---|
| `test_itineraries_returns_200` | El endpoint responde con HTTP 200 |
| `test_itineraries_returns_list` | La respuesta es una lista JSON |
| `test_itineraries_include_actividades` | Cada itinerario lleva su lista de actividades |
| `test_itineraries_include_user_and_dest_names` | Los JOINs con Usuarios y Destinos funcionan |
| `test_itineraries_fecha_format` | Las fechas tienen formato `YYYY-MM-DD` |

### 🔄 `TestPopulate` — Repoblado de BD (3 tests)
| Test | Qué verifica |
|---|---|
| `test_populate_returns_200` | Repoblar la BD devuelve HTTP 200 con mensaje |
| `test_destinations_exist_after_populate` | Hay destinos tras repoblar |
| `test_users_exist_after_populate` | Hay usuarios tras repoblar |

---

## Opciones útiles de pytest

```bash
# Ejecutar solo un grupo de tests
pytest tests/test_suite.py::TestUsers -v

# Ejecutar un test concreto
pytest tests/test_suite.py::TestUsers::test_create_user_returns_201 -v

# Parar al primer fallo
pytest tests/test_suite.py -v -x

# Ver print() dentro de los tests
pytest tests/test_suite.py -v -s

# Generar informe HTML (requiere: pip install pytest-html)
pytest tests/test_suite.py -v --html=tests/informe.html
```

---

## Si algún test falla

| Síntoma | Causa probable |
|---|---|
| `ConnectionRefusedError` | El servidor no está corriendo |
| `AssertionError: No hay destinos` | La BD está vacía — ejecuta POST `/api/v1/populate` |
| `assert status_code == 201, got 500` | Error en el servidor — revisa `docker compose logs backend` |
| Tests de populate muy lentos | Normal — genera 100 usuarios, destinos y eventos |

---

*Documentación de tests — Sprint 2 — ISI 2025/26*
