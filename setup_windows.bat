@echo off
setlocal

echo ============================================================
echo           SECURE MCP AGENT - WINDOWS SETUP
echo ============================================================
echo.

echo [1/6] Checking Python...
py --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python was not found.
    echo Please install Python 3.12 or 3.13 and run this script again.
    pause
    exit /b 1
)
py --version
echo.

echo [2/6] Creating virtual environment...
if not exist ".venv\Scripts\python.exe" (
    py -m venv .venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment.
        pause
        exit /b 1
    )
) else (
    echo Existing virtual environment found.
)
echo.

echo [3/6] Upgrading pip...
".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 (
    echo ERROR: Failed to upgrade pip.
    pause
    exit /b 1
)
echo.

echo [4/6] Installing project dependencies...
".venv\Scripts\python.exe" -m pip install -r requirements-windows.txt
if errorlevel 1 (
    echo ERROR: Dependency installation failed.
    pause
    exit /b 1
)
echo.

echo [5/6] Building knowledge base index...
".venv\Scripts\python.exe" knowledge_base\build_index.py
if errorlevel 1 (
    echo ERROR: Failed to build knowledge base index.
    pause
    exit /b 1
)
echo Knowledge base index created successfully.
echo.

echo [6/6] Checking Ollama...
where ollama >nul 2>&1
if errorlevel 1 (
    echo.
    echo WARNING: Ollama is not installed or not available in PATH.
    echo Ask the system administrator or mentor for approval before installing it.
    echo.
) else (
    ollama --version
    echo Ollama detected successfully.
)
echo.

echo ============================================================
echo                 SETUP COMPLETED
echo ============================================================
echo.
echo Next step: run run_demo.bat
echo.
pause