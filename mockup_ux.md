# TravelSense — Mockup GUI y User Experience

## 1. Visión General de la Interfaz

TravelSense tiene una **Single Page Application (SPA)** construida en `GUI/index.html`. La interfaz sigue un diseño moderno tipo "dashboard de viajes" con tema oscuro.

---

## 2. Pantallas / Secciones de la App

### 🏠 Pantalla 1: Inicio / Hero
```
┌──────────────────────────────────────────────────────┐
│  🌍  TravelSense                    [Logo]           │
│                                                      │
│  "Descubre tu próxima aventura"                      │
│                                                      │
│  [Explorar Destinos]  [Ver Itinerarios]              │
│                                                      │
│  ═══════════════ Estadísticas ════════════════       │
│    250+ Destinos  |  1000+ Eventos  |  100 Usuarios  │
└──────────────────────────────────────────────────────┘
```
**UX:** Landing visual de impacto con gradiente oscuro y llamadas a la acción prominentes.

---

### 🗺️ Pantalla 2: Explorador de Destinos
```
┌──────────────────────────────────────────────────────┐
│  🔍 [Buscar destino...]    Filtro: [Europa ▾]        │
│                                                      │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐              │
│  │Barcelona│  │  París  │  │  Tokio  │              │
│  │ 🌡 Suave│  │🌡Templad│  │🌡 Húmedo│              │
│  │España   │  │Francia  │  │ Japón   │              │
│  │[Ver más]│  │[Ver más]│  │[Ver más]│              │
│  └─────────┘  └─────────┘  └─────────┘              │
│                                                      │
│  [ Cargar más destinos ]                             │
└──────────────────────────────────────────────────────┘
```
**UX:** Grid de tarjetas con búsqueda en tiempo real y filtro por región. Las tarjetas tienen hover animation.

---

### 🎟️ Pantalla 3: Eventos por Destino
```
┌──────────────────────────────────────────────────────┐
│  Eventos en: [Selecciona ciudad ▾]                   │
│                                                      │
│  🎵 Festival Primavera Sound — Barcelona             │
│       Música | 180€                    [Ver]         │
│  ──────────────────────────────────────────          │
│  ⚽ FC Barcelona vs Valencia                         │
│       Deporte | 90€                    [Ver]         │
│  ──────────────────────────────────────────          │
│  🎨 Exposición Gaudí                                 │
│       Cultura | 25€                    [Ver]         │
└──────────────────────────────────────────────────────┘
```
**UX:** Lista filtrable de eventos con icono según categoría. Dropdown searchable para elegir ciudad.

---

### 📅 Pantalla 4: Mis Itinerarios
```
┌──────────────────────────────────────────────────────┐
│  Mis Itinerarios               [+ Nuevo Itinerario]  │
│                                                      │
│  ┌──────────────────────────────────────────┐        │
│  │ 📍 Barcelona            Jul 1 → Jul 7    │        │
│  │ 👤 María García      💰 1.200€           │        │
│  │ Actividades: Sagrada Familia, Tapas...   │        │
│  │                              [Ver detalle]│       │
│  └──────────────────────────────────────────┘        │
│                                                      │
│  ┌──────────────────────────────────────────┐        │
│  │ 📍 París               Ago 10 → Ago 17   │        │
│  │ 👤 Carlos Pérez      💰 2.400€           │        │
│  └──────────────────────────────────────────┘        │
└──────────────────────────────────────────────────────┘
```
**UX:** Cards expandibles con resumen de cada viaje. Botón flotante para crear nuevo itinerario.

---

### ⚙️ Pantalla 5: Administración (Populate DB)
```
┌──────────────────────────────────────────────────────┐
│  ⚙️  Panel de Administración                         │
│                                                      │
│  Base de datos actual:                               │
│    Usuarios: 100 | Destinos: 247 | Eventos: 1.200    │
│                                                      │
│  ⚠️  [Regenerar Base de Datos]                       │
│  Esto borrará todos los datos actuales y generará    │
│  nuevos datos de prueba con Faker.                   │
│                                                      │
│  Estado: ✅ Base de datos lista                      │
└──────────────────────────────────────────────────────┘
```
**UX:** Panel simple con confirmación antes de regenerar datos, con feedback visual del estado.

---

## 3. Mapa de Navegación (User Flow)

```
                    ┌─────────┐
                    │  INICIO │
                    └────┬────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
   ┌──────▼──────┐ ┌─────▼─────┐ ┌────▼──────┐
   │  Destinos   │ │  Eventos  │ │Itinerarios│
   └──────┬──────┘ └─────┬─────┘ └────┬──────┘
          │              │              │
   ┌──────▼──────┐       │       ┌────▼──────┐
   │ Detalle de  │       │       │  Detalle  │
   │  Destino    │       │       │Itinerario │
   └─────────────┘       │       └───────────┘
                    ┌─────▼─────┐
                    │  Filtrar  │
                    │ por ciudad│
                    └───────────┘
```

---

## 4. Decisiones de Diseño UX

| Principio | Implementación |
|---|---|
| **Simplicidad** | Navegación por secciones sin login requerido |
| **Rapidez** | API REST ligera, datos en JSON, sin recarga de página |
| **Descubribilidad** | Búsqueda y filtros visibles desde el primer momento |
| **Feedback** | Mensajes de éxito/error en todas las acciones |
| **Responsive** | Diseño adaptable a pantallas de escritorio y tablet |

---

## 5. Paleta de Colores y Tipografía

| Elemento | Valor |
|---|---|
| **Fondo principal** | `#1a1a2e` (azul muy oscuro) |
| **Acento primario** | `#0f3460` (azul marino) |
| **Acento secundario** | `#e94560` (rojo coral) |
| **Texto principal** | `#eaeaea` (blanco suave) |
| **Tipografía** | Inter / Roboto (Google Fonts) |
