@echo off
setlocal

echo ============================================================
echo       SECURE MCP AGENT - DEPLOYMENT PRE-FLIGHT CHECK
echo ============================================================
echo.

echo [1/6] Checking Python...
py --version >nul 2>&1
if errorlevel 1 (
    echo STATUS: MISSING - Python launcher not found.
) else (
    echo STATUS: READY
    py --version
)
echo.

echo [2/6] Checking Git...
git --version >nul 2>&1
if errorlevel 1 (
    echo STATUS: MISSING - Git not found.
) else (
    echo STATUS: READY
    git --version
)
echo.

echo [3/6] Checking required project files and artifacts...
set FILES_OK=1

if not exist "demo.py" (
    echo MISSING: demo.py
    set FILES_OK=0
)

if not exist "requirements-windows.txt" (
    echo MISSING: requirements-windows.txt
    set FILES_OK=0
)

if not exist "knowledge_base\vectorstore\security_index.faiss" (
    echo NOT BUILT: security_index.faiss - setup will generate it.
)

if not exist "knowledge_base\vectorstore\documents.txt" (
    echo NOT BUILT: documents.txt - setup will generate it.
)

if "%FILES_OK%"=="1" (
    echo STATUS: READY - Required project files found.
)
echo.

echo [4/6] Checking virtual environment...
if exist ".venv\Scripts\python.exe" (
    echo STATUS: READY - Virtual environment found.
) else (
    echo STATUS: NOT SET UP - Run setup_windows.bat.
)
echo.

echo [5/6] Checking Ollama...
where ollama >nul 2>&1
if errorlevel 1 (
    echo STATUS: MISSING - Ollama not found.
) else (
    echo STATUS: READY
    ollama --version
)
echo.

echo [6/6] Checking llama3.2:3b model...
where ollama >nul 2>&1
if errorlevel 1 (
    echo STATUS: NOT CHECKED - Ollama is unavailable.
) else (
    ollama list | findstr /C:"llama3.2:3b" >nul 2>&1
    if errorlevel 1 (
        echo STATUS: MISSING - Required model not found.
    ) else (
        echo STATUS: READY - llama3.2:3b found.
    )
)
echo.

echo ============================================================
echo                 PRE-FLIGHT CHECK COMPLETE
echo ============================================================
echo.
echo Review any MISSING or NOT SET UP items before running the demo.
echo.
pause