@echo off
setlocal

echo ============================================================
echo          SECURE MCP AGENT - DEMO LAUNCHER
echo ============================================================
echo.

echo [1/3] Checking project environment...
if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Project environment not found.
    echo Run setup_windows.bat first.
    pause
    exit /b 1
)
echo Environment found.
echo.

echo [2/3] Checking Ollama...
where ollama >nul 2>&1
if errorlevel 1 (
    echo ERROR: Ollama is not installed or not available in PATH.
    echo The RAG agent demo requires Ollama.
    pause
    exit /b 1
)

ollama list | findstr /C:"llama3.2:3b" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Required model llama3.2:3b was not found.
    echo The model must be made available through the approved setup process.
    pause
    exit /b 1
)

echo Ollama and llama3.2:3b detected.
echo.

echo [3/3] Starting Secure MCP Agent demonstration...
echo.

".venv\Scripts\python.exe" demo.py

if errorlevel 1 (
    echo.
    echo ERROR: Demo execution failed.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo              DEMONSTRATION FINISHED
echo ============================================================
echo.
pause