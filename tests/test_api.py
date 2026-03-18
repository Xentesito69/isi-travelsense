"""
test_api.py - TravelSense
Pruebas de integracion para los endpoints de la API REST.

USO:
  1. Arranca primero el servidor: py backend/app.py
  2. Luego en otra terminal: py tests/test_api.py
"""

import requests
import json
import sys

# Fix encoding for Windows terminal
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE_URL = "http://127.0.0.1:5000/api/v1"

def print_section(title):
    print(f"\n{'='*50}")
    print(f"  {title}")
    print(f"{'='*50}")

def test_get_users():
    print_section("TEST: GET /users")
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200, f"Error: status {response.status_code}"
    users = response.json()
    assert isinstance(users, list), "La respuesta debe ser una lista"
    print(f"[OK] Se recuperaron {len(users)} usuarios")
    if users:
        print(f"   Ejemplo: {json.dumps(users[0], ensure_ascii=False, indent=4)}")
    return users

def test_create_user():
    print_section("TEST: POST /users")
    payload = {
        "nombre": "Test TravelSense",
        "email": "test@travelsense.es",
        "preferencias": "playa, gastronomia, cultura"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201, f"Error: status {response.status_code}"
    data = response.json()
    assert "id" in data, "La respuesta debe contener 'id'"
    assert data["nombre"] == payload["nombre"]
    print(f"[OK] Usuario creado con ID {data['id']}")
    return data["id"]

def test_get_destinations():
    print_section("TEST: GET /destinations")
    response = requests.get(f"{BASE_URL}/destinations")
    assert response.status_code == 200, f"Error: status {response.status_code}"
    dests = response.json()
    assert isinstance(dests, list), "La respuesta debe ser una lista"
    print(f"[OK] Se recuperaron {len(dests)} destinos")
    if dests:
        print(f"   Ejemplo: {json.dumps(dests[0], ensure_ascii=False, indent=4)}")
    return dests

def test_get_events():
    print_section("TEST: GET /events")
    response = requests.get(f"{BASE_URL}/events")
    assert response.status_code == 200, f"Error: status {response.status_code}"
    events = response.json()
    assert isinstance(events, list), "La respuesta debe ser una lista"
    print(f"[OK] Se recuperaron {len(events)} eventos")
    if events:
        print(f"   Ejemplo: {json.dumps(events[0], ensure_ascii=False, indent=4)}")
    return events

def test_get_itineraries():
    print_section("TEST: GET /itineraries")
    response = requests.get(f"{BASE_URL}/itineraries")
    assert response.status_code == 200, f"Error: status {response.status_code}"
    itins = response.json()
    assert isinstance(itins, list), "La respuesta debe ser una lista"
    print(f"[OK] Se recuperaron {len(itins)} itinerarios")
    if itins:
        sample = itins[0]
        assert "actividades" in sample, "Cada itinerario debe incluir 'actividades'"
        assert "usuario_nombre" in sample, "Cada itinerario debe incluir 'usuario_nombre'"
        assert "destino_nombre" in sample, "Cada itinerario debe incluir 'destino_nombre'"
        print(f"   Destino: {sample['destino_nombre']} | Actividades: {len(sample['actividades'])}")
    return itins

def run_all_tests():
    print("\nTravelSense - Suite de Tests de la API")
    print("Asegurate de que el servidor esta corriendo en http://127.0.0.1:5000")

    passed = 0
    failed = 0

    tests = [
        ("GET /users", test_get_users),
        ("POST /users", test_create_user),
        ("GET /destinations", test_get_destinations),
        ("GET /events", test_get_events),
        ("GET /itineraries", test_get_itineraries),
    ]

    for name, test_fn in tests:
        try:
            test_fn()
            passed += 1
        except AssertionError as e:
            print(f"[FALLO] {name}: {e}")
            failed += 1
        except Exception as e:
            print(f"[ERROR] {name}: {e}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"  RESULTADO: {passed} PASADOS | {failed} FALLIDOS")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    run_all_tests()
