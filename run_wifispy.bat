@echo off
title WifiSpy v2.0 by MD-HACKER
color 0a

echo.
echo  __        ___ ___ _  ___ ____   __ 
echo  \ \      / (_) __(_)/ __|  _ \ / _|
echo   \ \ /\ / /| | _| _| (__| |_) | |_ 
echo    \ V  V / | ||_|| |\___| .__/|  _|
echo     \_/\_/  |_|  |_|     |_|   |_|   
echo.
echo         Version 2.0 - By MD-HACKER
echo.
echo  GitHub: https://github.com/MD-HACKER07
echo  Website: https://abushalem.site/
echo.
echo ---------------------------------------------
echo.

REM Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found. Please install Python 3.9 or higher.
    echo     Visit https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Check if running as administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] This script requires administrator privileges.
    echo     Please run as administrator.
    echo.
    pause
    exit /b 1
)

echo [+] Starting WifiSpy...
echo.

if "%~1"=="" (
    echo [i] No arguments provided. Starting in interactive mode.
    echo.
    python bin\wifispy
) else (
    echo [i] Starting with provided arguments.
    echo.
    python bin\wifispy %*
)

if %errorlevel% neq 0 (
    echo.
    echo [!] WifiSpy exited with an error. Check the logs for details.
    echo.
)

pause 