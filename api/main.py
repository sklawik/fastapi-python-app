from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, APIRouter

app = FastAPI()


@app.get("/")
async def root():
    return HTMLResponse(content="Welcome to FastAPI!", status_code=200)
router = APIRouter()

class SecondItem(BaseModel):
    title: str
    arr: [{
        arr: List[neste]
    }]

class Item(BaseModel):
    id: int
    name: str
    price: float



@router.get("/items", response_model=List[Item])
async def get_items():
    return [
        {"id": 1, "name": "Item A", "price": 9.99},
        {"id": 2, "name": "Item B", "price": 19.99},
        {"id": 3, "name": "Item C", "price": 29.99},
    ]


@router.get("/alerts/{branch}", response_model=Item)
async def get_alerts():
    return []

app.include_router(router)

