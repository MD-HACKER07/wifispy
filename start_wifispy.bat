@echo off
echo Starting WifiSpy...

set PYTHONPATH=%CD%;%PYTHONPATH%
cd %~dp0
python bin\wifispy %*
pause 