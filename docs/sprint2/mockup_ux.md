# TravelSense — Mockup GUI y User Experience

## 1. Visión General

TravelSense tiene una **Single Page Application (SPA)** en `GUI/index.html`. Diseño moderno tipo dashboard de viajes con tema oscuro.

---

## 2. Pantallas Principales

### 🏠 Inicio / Hero
<img width="1919" height="1019" alt="Captura de pantalla 2026-03-21 185701" src="https://github.com/user-attachments/assets/e9c44f27-b5ca-45e6-9dac-3bfa62ade02a" />

### 🗺️ Explorador de Destinos

<img width="1919" height="1014" alt="Captura de pantalla 2026-03-21 185749" src="https://github.com/user-attachments/assets/26635f0f-8f4c-4ecc-87b8-d653ea46fa9a" />

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
