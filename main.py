from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


htmlFile=""

with open("./main.html", 'r') as file:
    htmlFile = file.read()

@app.get('/')
async def root():
    return HTMLResponse(content=htmlFile)