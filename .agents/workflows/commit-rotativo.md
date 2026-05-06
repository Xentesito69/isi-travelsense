---
description: commit and push changes to GitHub rotating between the 3 contributors
---

# Commit Rotativo entre Contribuidores

Cada vez que se hace un cambio que funciona, se sube con uno de los 3 autores del equipo, elegido al azar.

## Contribuidores

| Usuario | Email git |
|---|---|
| noeliaasanchezc | noeliaasanchezc@users.noreply.github.com |
| Mariam770ts | Mariam770ts@users.noreply.github.com |
| Xentesito69 | Xentesito69@users.noreply.github.com |

## Pasos

// turbo-all
1. Selecciona un contribuidor al azar (diferente al del último commit si es posible)

2. Haz stage de los archivos modificados:
```powershell
git add <archivos>
```

3. Haz commit con el autor rotativo:
```powershell
git -c user.name="<USERNAME>" -c user.email="<EMAIL>" commit -m "<mensaje descriptivo en inglés>"
```

4. Haz push a main:
```powershell
git push origin main
```

## Reglas

- El mensaje del commit debe ser en inglés, descriptivo y con prefijo tipo: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`
- Elegir uno de los 3 autores completamente al azar (puede repetirse)
- Siempre hacer push a la rama `main`
- El working directory del repositorio es: `c:\Users\vicen\Downloads\IsiAntigravity`
