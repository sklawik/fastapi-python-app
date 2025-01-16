from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


class LinkedList:
    def __init__(self):
        print("class init")
    

class Node:
    value: int
    parent: Node
    children: Node
    def __init__(value):
        
        

htmlFile=""

with open("./main.html", 'r') as file:
    htmlFile = file.read()

@app.get('/')
async def root():
    return HTMLResponse(content=htmlFile)