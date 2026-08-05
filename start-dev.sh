#!/bin/bash
source .venv/bin/activate
python3 -c "import fastapi; import uvicorn"
if [ $? -eq 0 ]; then
    echo 'Znaleziono FastAPI'
else
    echo 'Nie znaleziono FastAPI lub uvicorn. Instalacja:'
    python3 -m venv .venv
    source .venv/bin/activate
    pip install fastapi
    pip install uvicorn
fi

echo 'uruchamianie skryptu..'
open "http://localhost:8000"
uvicorn main:app --reload
