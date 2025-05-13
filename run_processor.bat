@echo off
REM Simple script to run the data processor

REM Check if input file is provided
if "%~1"=="" (
    echo Please provide an input file
    echo Example: run_processor.bat test_data.csv
    exit /b 1
)

REM Run the Python script
python data_processor.py "%~1"

echo Done! 