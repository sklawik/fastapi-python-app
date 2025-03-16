#!/bin/bash
python3 -c "import fastapi uvicorn"
if [ $? -eq 0 ]; then
    echo 'Znaleziono FastAPI'
else
    echo 'Nie znaleziono FastAPI lub uvicorn. Instalacja:'
    pip3 install fastapi
    pip3 install uvicorn
fi

echo 'uruchamianie skryptu..'
open "http://localhost:8000"
python3 -m uvicorn main:app --reload