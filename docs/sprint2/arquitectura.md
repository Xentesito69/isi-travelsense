# TravelSense — Arquitectura Global

## Visión General

TravelSense es una aplicación web cliente-servidor con arquitectura en **3 capas**:

```
┌──────────────────────────────────────────────────────┐
│               CAPA DE PRESENTACIÓN                   │
│          Frontend: HTML + CSS + JavaScript            │
│              (GUI/index.html)                         │
└───────────────────┬──────────────────────────────────┘
                    │  HTTP / REST (JSON)
                    │  fetch() / AJAX
┌───────────────────▼──────────────────────────────────┐
│               CAPA DE NEGOCIO                         │
│           Backend: Python / Flask                     │
│              (app.py, database.py)                    │
│    Endpoints: /api/v1/users, /destinations,           │
│               /events, /itineraries, /populate        │
└───────────────────┬──────────────────────────────────┘
                    │  sqlite3 (Python built-in)
┌───────────────────▼──────────────────────────────────┐
│               CAPA DE DATOS                           │
│           SQLite — travelsense.db                     │
│  Tablas: Usuarios, Destinos, Eventos,                 │
│          Itinerarios, Actividades                     │
└──────────────────────────────────────────────────────┘
```

---

## Componentes Principales

| Componente | Archivo(s) | Responsabilidad |
|---|---|---|
| **API Server** | `app.py` | Define todos los endpoints REST con Flask |
| **Database Helper** | `database.py` | Funciones reutilizables de acceso a SQLite |
| **DB Setup** | `setup_database.py` | Crea tablas e inserta datos iniciales |
| **Data Pool** | `datos_viaje.py` | Diccionario con ~250 destinos y eventos por ciudad |
| **Event Generator** | `generador.py` | Lógica de generación de itinerarios/actividades |
| **Frontend** | `GUI/index.html` | Interfaz web completa (SPA en HTML/JS) |
| **Coords Helper** | `coords.js` | Coordenadas geográficas de destinos para mapas |

---

## Flujo de Datos Principal

### Consulta de Destinos (ejemplo)
```
Usuario → abre la web (index.html)
  → JavaScript llama: GET http://localhost:5000/api/v1/destinations
  → Flask (app.py) recibe la petición
  → Consulta SQLite: SELECT * FROM Destinos
  → Devuelve JSON con la lista de destinos
  → JavaScript renderiza las tarjetas en el HTML
```

---

## Diagrama para diagrams.net (XML importable)

Importa este XML en https://app.diagrams.net/ → Extras → Edit Diagram:

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="FRONTEND&#xa;HTML / CSS / JavaScript&#xa;(GUI/index.html)" style="rounded=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;" vertex="1" parent="1">
      <mxGeometry x="300" y="40" width="240" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="BACKEND&#xa;Python / Flask&#xa;(app.py)" style="rounded=1;fillColor=#d5e8d4;strokeColor=#82b366;fontStyle=1;fontSize=12;" vertex="1" parent="1">
      <mxGeometry x="300" y="200" width="240" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="4" value="BASE DE DATOS&#xa;SQLite&#xa;(travelsense.db)" style="shape=cylinder3;fillColor=#ffe6cc;strokeColor=#d6b656;fontStyle=1;fontSize=12;" vertex="1" parent="1">
      <mxGeometry x="320" y="370" width="200" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="datos_viaje.py&#xa;Pool de ~250 destinos&#xa;y eventos" style="rounded=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="1">
      <mxGeometry x="620" y="200" width="180" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="setup_database.py&#xa;Crea tablas e inserta&#xa;datos iniciales" style="rounded=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=11;" vertex="1" parent="1">
      <mxGeometry x="60" y="200" width="180" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="8" value="HTTP REST (JSON)&#xa;fetch() / AJAX" style="edgeStyle=orthogonalEdgeStyle;" edge="1" source="2" target="3" parent="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="sqlite3 (Python)" style="edgeStyle=orthogonalEdgeStyle;" edge="1" source="3" target="4" parent="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="import" style="edgeStyle=orthogonalEdgeStyle;dashed=1;" edge="1" source="5" target="3" parent="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="11" value="crea tablas" style="edgeStyle=orthogonalEdgeStyle;dashed=1;" edge="1" source="6" target="4" parent="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>
```

---

## Endpoints API REST

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/v1/users` | Lista todos los usuarios |
| POST | `/api/v1/users` | Crea un usuario |
| GET | `/api/v1/destinations` | Lista todos los destinos |
| GET | `/api/v1/events` | Lista todos los eventos (con nombre de destino) |
| GET | `/api/v1/itineraries` | Lista itinerarios con actividades |
| POST | `/api/v1/populate` | Regenera la base de datos con datos de prueba |
