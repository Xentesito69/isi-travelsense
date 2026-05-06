"""
test_suite.py — TravelSense · Suite completa de tests
======================================================
20 tests que cubren:
  - Estructura y formato de respuestas (JSON, listas, campos)
  - Lógica de negocio (conteos, relaciones entre entidades)
  - Gestión de usuarios (creación, validación, duplicados)
  - Endpoints de escritura y lectura
  - Manejo de errores y entradas inválidas
  - Repoblado de la BD

Ejecutar:
    pip install pytest requests
    pytest tests/test_suite.py -v
"""

import pytest
import requests
import time

BASE = "http://127.0.0.1:5000/api/v1"
TIMEOUT = 10  # segundos por petición


# ──────────────────────────────────────────────────────────────────────────────
# FIXTURES
# ──────────────────────────────────────────────────────────────────────────────

@pytest.fixture(scope="session", autouse=True)
def check_server():
    """Verifica que el servidor está corriendo antes de lanzar ningún test."""
    try:
        r = requests.get(f"{BASE}/destinations", timeout=5)
        r.raise_for_status()
    except Exception:
        pytest.exit(
            "\n[ERROR] El servidor no está corriendo en http://127.0.0.1:5000\n"
            "Arráncalo primero con:  python backend/app.py\n"
            "  o con Docker:         docker compose up -d\n",
            returncode=1
        )


@pytest.fixture(scope="session")
def destinations():
    return requests.get(f"{BASE}/destinations", timeout=TIMEOUT).json()


@pytest.fixture(scope="session")
def users():
    return requests.get(f"{BASE}/users", timeout=TIMEOUT).json()


@pytest.fixture(scope="session")
def events():
    return requests.get(f"{BASE}/events", timeout=TIMEOUT).json()


@pytest.fixture(scope="session")
def itineraries():
    return requests.get(f"{BASE}/itineraries", timeout=TIMEOUT).json()


# ──────────────────────────────────────────────────────────────────────────────
# 1. DESTINOS
# ──────────────────────────────────────────────────────────────────────────────

class TestDestinations:

    def test_destinations_returns_200(self):
        """GET /destinations debe devolver código 200."""
        r = requests.get(f"{BASE}/destinations", timeout=TIMEOUT)
        assert r.status_code == 200

    def test_destinations_returns_list(self, destinations):
        """GET /destinations debe devolver una lista JSON."""
        assert isinstance(destinations, list)

    def test_destinations_not_empty(self, destinations):
        """La BD debe tener al menos 1 destino."""
        assert len(destinations) > 0, "No hay destinos en la base de datos"

    def test_destinations_have_required_fields(self, destinations):
        """Cada destino debe tener id, nombre, pais y region."""
        required = {"id", "nombre", "pais", "region"}
        for dest in destinations:
            missing = required - dest.keys()
            assert not missing, f"Destino sin campos: {missing} → {dest}"

    def test_destinations_nombre_not_empty(self, destinations):
        """El campo 'nombre' de cada destino no debe estar vacío."""
        for dest in destinations:
            assert dest["nombre"], f"Destino con nombre vacío: {dest}"


# ──────────────────────────────────────────────────────────────────────────────
# 2. USUARIOS
# ──────────────────────────────────────────────────────────────────────────────

class TestUsers:

    def test_users_returns_200(self):
        """GET /users debe devolver código 200."""
        r = requests.get(f"{BASE}/users", timeout=TIMEOUT)
        assert r.status_code == 200

    def test_users_returns_list(self, users):
        """GET /users debe devolver una lista JSON."""
        assert isinstance(users, list)

    def test_users_have_required_fields(self, users):
        """Cada usuario debe tener al menos id, nombre y email."""
        required = {"id", "nombre", "email"}
        for user in users:
            missing = required - user.keys()
            assert not missing, f"Usuario sin campos: {missing} → {user}"

    def test_create_user_returns_201(self):
        """POST /users con datos válidos debe devolver 201."""
        ts = int(time.time())
        payload = {
            "nombre": f"Usuario Test {ts}",
            "email": f"test_{ts}@travelsense.es",
            "preferencias": "Playa, Cultura"
        }
        r = requests.post(f"{BASE}/users", json=payload, timeout=TIMEOUT)
        assert r.status_code == 201

    def test_create_user_returns_id(self):
        """El usuario creado debe tener un 'id' numérico en la respuesta."""
        ts = int(time.time()) + 1
        payload = {
            "nombre": f"Usuario ID {ts}",
            "email": f"id_{ts}@travelsense.es"
        }
        r = requests.post(f"{BASE}/users", json=payload, timeout=TIMEOUT)
        data = r.json()
        assert "id" in data
        assert isinstance(data["id"], int)

    def test_create_user_nombre_matches(self):
        """El nombre del usuario creado debe coincidir con el enviado."""
        ts = int(time.time()) + 2
        nombre = f"Comprobacion {ts}"
        payload = {"nombre": nombre, "email": f"match_{ts}@travelsense.es"}
        r = requests.post(f"{BASE}/users", json=payload, timeout=TIMEOUT)
        assert r.json()["nombre"] == nombre

    def test_create_user_missing_nombre_returns_400(self):
        """POST /users sin 'nombre' debe devolver 400."""
        r = requests.post(f"{BASE}/users", json={"email": "sin_nombre@x.com"}, timeout=TIMEOUT)
        assert r.status_code == 400


# ──────────────────────────────────────────────────────────────────────────────
# 3. EVENTOS
# ──────────────────────────────────────────────────────────────────────────────

class TestEvents:

    def test_events_returns_200(self):
        """GET /events debe devolver código 200."""
        r = requests.get(f"{BASE}/events", timeout=TIMEOUT)
        assert r.status_code == 200

    def test_events_returns_list(self, events):
        """GET /events debe devolver una lista JSON."""
        assert isinstance(events, list)

    def test_events_not_empty(self, events):
        """La BD debe tener al menos 1 evento."""
        assert len(events) > 0, "No hay eventos en la base de datos"

    def test_events_have_destino_nombre(self, events):
        """Cada evento debe incluir el campo 'destino_nombre' (join con Destinos)."""
        for event in events:
            assert "destino_nombre" in event, f"Evento sin 'destino_nombre': {event}"

    def test_events_have_required_fields(self, events):
        """Cada evento debe tener id, nombre, tipo, fecha y precio."""
        required = {"id", "nombre", "tipo", "fecha", "precio"}
        for event in events:
            missing = required - event.keys()
            assert not missing, f"Evento sin campos: {missing}"


# ──────────────────────────────────────────────────────────────────────────────
# 4. ITINERARIOS
# ──────────────────────────────────────────────────────────────────────────────

class TestItineraries:

    def test_itineraries_returns_200(self):
        """GET /itineraries debe devolver código 200."""
        r = requests.get(f"{BASE}/itineraries", timeout=TIMEOUT)
        assert r.status_code == 200

    def test_itineraries_returns_list(self, itineraries):
        """GET /itineraries debe devolver una lista JSON."""
        assert isinstance(itineraries, list)

    def test_itineraries_include_actividades(self, itineraries):
        """Cada itinerario debe incluir su lista de actividades."""
        if not itineraries:
            pytest.skip("No hay itinerarios en la BD")
        for it in itineraries:
            assert "actividades" in it, f"Itinerario sin 'actividades': {it['id']}"
            assert isinstance(it["actividades"], list)

    def test_itineraries_include_user_and_dest_names(self, itineraries):
        """Cada itinerario debe incluir usuario_nombre y destino_nombre (joins)."""
        if not itineraries:
            pytest.skip("No hay itinerarios en la BD")
        for it in itineraries:
            assert "usuario_nombre" in it
            assert "destino_nombre" in it

    def test_itineraries_fecha_format(self, itineraries):
        """El campo 'fecha' debe tener formato YYYY-MM-DD."""
        import re
        pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
        if not itineraries:
            pytest.skip("No hay itinerarios en la BD")
        for it in itineraries:
            assert pattern.match(it["fecha"]), f"Fecha con formato incorrecto: {it['fecha']}"


# ──────────────────────────────────────────────────────────────────────────────
# 5. POPULATE (repoblado de la BD)
# ──────────────────────────────────────────────────────────────────────────────

class TestPopulate:

    def test_populate_returns_200(self):
        """POST /populate debe devolver 200 y un mensaje de éxito."""
        r = requests.post(f"{BASE}/populate", timeout=60)
        assert r.status_code == 200
        data = r.json()
        assert "message" in data

    def test_destinations_exist_after_populate(self):
        """Tras repoblar, debe haber destinos en la BD."""
        r = requests.get(f"{BASE}/destinations", timeout=TIMEOUT)
        assert len(r.json()) > 0

    def test_users_exist_after_populate(self):
        """Tras repoblar, debe haber usuarios en la BD."""
        r = requests.get(f"{BASE}/users", timeout=TIMEOUT)
        assert len(r.json()) > 0
