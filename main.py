from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

class Node:
    value: int
    parent: Node
    children: Node
    def __init__(value):
        

class LinkedList:
    rootNode: Node
    def __init__(self):
        print("class init")
    


        

htmlFile=""

with open("./main.html", 'r') as file:
    htmlFile = file.read()

@app.get('/')
async def root():
    return HTMLResponse(content=htmlFile)