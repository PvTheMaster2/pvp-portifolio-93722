@echo off
echo ========================================
echo    PDF Cropper - Instalacao Windows
echo ========================================
echo.

echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python nao encontrado!
    echo Por favor, instale Python 3.7+ de: https://python.org
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

echo Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Erro ao instalar dependencias
    echo Tente executar: pip install --upgrade pip
    pause
    exit /b 1
)

echo ✅ Dependencias instaladas com sucesso!
echo.

echo Testando instalacao...
python pdf_cropper.py --help

if errorlevel 1 (
    echo ❌ Erro no teste de instalacao
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ Instalacao concluida com sucesso!
echo ========================================
echo.
echo Como usar:
echo   python pdf_cropper.py --input "seu_arquivo.pdf" --interactive
echo.
echo Para mais informacoes, consulte o README.md
echo.
pause 