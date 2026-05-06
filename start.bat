@echo off
title TravelSense - Iniciando...
echo.
echo  ==========================================
echo   TravelSense - IsiAntigravity
echo  ==========================================
echo.

:: ---- Detectar Python ----
set PYTHON_CMD=
where py >nul 2>&1 && set PYTHON_CMD=py
if "%PYTHON_CMD%"=="" where python >nul 2>&1 && set PYTHON_CMD=python
if "%PYTHON_CMD%"=="" where python3 >nul 2>&1 && set PYTHON_CMD=python3

if "%PYTHON_CMD%"=="" (
    echo [ERROR] Python no encontrado en tu sistema.
    echo.
    echo  Instala Python desde: https://www.python.org/downloads/
    echo  Asegurate de marcar "Add Python to PATH" al instalar.
    echo.
    pause
    exit /b 1
)

echo  [OK] Python encontrado: %PYTHON_CMD%
echo.

:: ---- Instalar dependencias si faltan ----
echo  Verificando dependencias del backend...
%PYTHON_CMD% -m pip install -r backend\requirements.txt -q --disable-pip-version-check
if errorlevel 1 (
    echo [AVISO] Hubo un problema instalando dependencias.
    echo  Intentando continuar de todas formas...
)
echo  [OK] Dependencias listas.
echo.

:: ---- Crear .env si no existe ----
if not exist backend\.env (
    echo  [AVISO] No se encontro backend\.env - creando uno de ejemplo...
    copy backend\.env.example backend\.env >nul 2>&1
    echo  [!] Edita backend\.env con tu GOOGLE_CLIENT_ID y GEMINI_API_KEY
    echo.
)

:: ---- Lanzar Backend (puerto 5000) ----
echo  Iniciando Backend en http://localhost:5000 ...
start "TravelSense Backend" cmd /k "cd backend && %PYTHON_CMD% app.py"

:: ---- Esperar 2 segundos a que arranque el backend ----
timeout /t 2 >nul

:: ---- Lanzar Frontend (puerto 8000) ----
echo  Iniciando Frontend en http://localhost:8000 ...
start "TravelSense Frontend" cmd /k "cd frontend && %PYTHON_CMD% -m http.server 8000 --bind 127.0.0.1"

:: ---- Abrir navegador ----
timeout /t 2 >nul
echo.
echo  ==========================================
echo   Abriendo TravelSense en tu navegador...
echo  ==========================================
echo.
start http://localhost:8000

echo  Si no se abre, ve manualmente a: http://localhost:8000
echo  Para cerrar la app, cierra las dos ventanas de consola.
echo.
pause
