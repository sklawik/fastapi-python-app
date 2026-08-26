from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

todos = [
        {"id": "1",
         "title": "Welcome to FastAPI!",
         "description":"Test"}
     ]


@app.get("/todos")
async def root():
    global todos
    return todos
     
     
@app.delete("/todos")
async def delete_todo(id: str):
    global todos
    todos = [todo for todo in todos if todo["id"] != id]
    return todos

@app.post("/todos")
async def create_todo(todo: dict):
    global todos
    todos.append(todo)
    return todos
