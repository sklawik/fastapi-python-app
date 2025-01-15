#!/bin/bash
python3 -c "import fastapi uvicorn"
if [ $? -eq 0 ]; then
    echo 'Znaleziono FastAPI'
else
    echo 'Nie znaleziono FastAPI lub uvicorn. Instalacja:'
    pipx install fastapi
    pipx install uvicorn
fi

echo 'uruchamianie skryptu..'
open "http://localhost:8000"
uvicorn main:app --reload
