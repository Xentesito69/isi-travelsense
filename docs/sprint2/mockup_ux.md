# TravelSense — Mockup GUI y User Experience

## 1. Visión General

TravelSense tiene una **Single Page Application (SPA)** en `GUI/index.html`. Diseño moderno tipo dashboard de viajes con tema oscuro.

---

## 2. Pantallas Principales

### 🏠 Inicio / Hero
```
┌──────────────────────────────────────────────────────┐
│  🌍  TravelSense                         [Logo]      │
│                                                      │
│         "Descubre tu próxima aventura"               │
│                                                      │
│     [Explorar Destinos]   [Ver Itinerarios]          │
│                                                      │
│   250+ Destinos  |  1000+ Eventos  |  100 Usuarios   │
└──────────────────────────────────────────────────────┘
```

### 🗺️ Explorador de Destinos
```
┌──────────────────────────────────────────────────────┐
│  🔍 [Buscar destino...]     Filtro: [Europa ▾]       │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │Barcelona │  │  París   │  │  Tokio   │           │
│  │🌡 Suave  │  │🌡Templado│  │🌡 Húmedo │           │
│  │ España   │  │ Francia  │  │  Japón   │           │
│  │ [Ver más]│  │ [Ver más]│  │ [Ver más]│           │
│  └──────────┘  └──────────┘  └──────────┘           │
└──────────────────────────────────────────────────────┘
```
**UX:** Grid de tarjetas con búsqueda en tiempo real y hover animation.

### 🎟️ Eventos por Destino
```
┌──────────────────────────────────────────────────────┐
│  Eventos en: [Selecciona ciudad ▾]                   │
│                                                      │
│  🎵 Festival Primavera Sound   Música  | 180€  [Ver] │
│  ──────────────────────────────────────────          │
│  ⚽ FC Barcelona vs Valencia   Deporte | 90€   [Ver] │
│  ──────────────────────────────────────────          │
│  🎨 Exposición Gaudí           Cultura | 25€   [Ver] │
└──────────────────────────────────────────────────────┘
```

### 📅 Mis Itinerarios
```
┌──────────────────────────────────────────────────────┐
│  Mis Itinerarios               [+ Nuevo Itinerario]  │
│                                                      │
│  ┌────────────────────────────────────────────┐      │
│  │ 📍 Barcelona          Jul 1 → Jul 7        │      │
│  │ 👤 María García    💰 1.200€               │      │
│  │ Actividades: Sagrada Familia, Tapas...     │      │
│  │                           [Ver detalle]   │      │
│  └────────────────────────────────────────────┘      │
└──────────────────────────────────────────────────────┘
```

---

## 3. Mapa de Navegación

```
              ┌─────────┐
              │  INICIO │
              └────┬────┘
                   │
     ┌─────────────┼─────────────┐
     │             │             │
┌────▼────┐  ┌─────▼─────┐  ┌──▼──────────┐
│Destinos │  │  Eventos  │  │ Itinerarios │
└────┬────┘  └─────┬─────┘  └──┬──────────┘
     │              │           │
┌────▼────┐   ┌─────▼───┐  ┌──▼──────────┐
│ Detalle │   │ Filtrar │  │   Detalle   │
│Destino  │   │ Ciudad  │  │ Itinerario  │
└─────────┘   └─────────┘  └─────────────┘
```

---

## 4. Decisiones de Diseño UX

| Principio | Implementación |
|---|---|
| **Simplicidad** | Sin login requerido en fase de prototipo |
| **Rapidez** | API REST ligera, sin recarga de página |
| **Descubribilidad** | Búsqueda y filtros visibles desde el primer momento |
| **Feedback** | Mensajes éxito/error en todas las acciones |
| **Responsive** | Diseño adaptable a escritorio y tablet |

---

## 5. Paleta de Colores

| Elemento | Valor |
|---|---|
| **Fondo principal** | `#1a1a2e` (azul muy oscuro) |
| **Acento primario** | `#0f3460` (azul marino) |
| **Acento secundario** | `#e94560` (rojo coral) |
| **Texto principal** | `#eaeaea` (blanco suave) |
| **Tipografía** | Inter / Roboto (Google Fonts) |
