@echo off
chcp 65001 >nul
cd /d "%~dp0"
net session >nul 2>&1
if %errorlevel%==0 (
    netsh advfirewall firewall delete rule name="LongoUZ 6060" >nul 2>&1
    netsh advfirewall firewall delete rule name="LongoUZ 6600" >nul 2>&1
    netsh advfirewall firewall add rule name="LongoUZ 6060" dir=in action=allow protocol=TCP localport=6060 profile=any >nul
    netsh advfirewall firewall add rule name="LongoUZ 6600" dir=in action=allow protocol=TCP localport=6600 profile=any >nul
    echo [OK] Windows Firewall: 6060 va 6600 portlari ochildi.
) else (
    echo [!] Administrator huquqi yo'q: firewall qoidasi qo'shilmadi.
    echo     Boshqa qurilmadan kirib bo'lmasa, shu faylni "Run as administrator" bilan BIR MARTA ishga tushiring.
)

python main.py
pause
