#!/bin/bash
python3 -c "import fastapi"
if [ $? -eq 0 ]; then
    echo 'Znaleziono FastAPI'
else
    echo 'Nie znaleziono FastAPI. Instalacja:'
    pipx install fastapi
fi

echo 'uruchamianie skryptu..'
python3 ./main.py