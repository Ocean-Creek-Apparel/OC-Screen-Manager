@echo off
REM Simple Database Backup to D: Drive
REM Backs up the database to D:\backups with timestamp

REM Check if D: drive exists
if not exist D:\ (
    exit /b 0
)

REM Create backups folder on D: drive if it doesn't exist
if not exist D:\backups mkdir D:\backups

REM Get timestamp for backup filename
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c%%a%%b)
for /f "tokens=1-2 delims=/: " %%a in ('time /t') do (set mytime=%%a%%b)
set timestamp=%mydate%_%mytime%

REM Copy database file with timestamp
copy "DATABASE_PATH_GOES_HERE" "D:\backups\screen_database_backup_%timestamp%.db"

REM Delete backups older than 14 days
forfiles /P "D:\backups" /M test_data_backup_*.db /D -14 /C "cmd /c del @path" 2>nul

exit /b 0
