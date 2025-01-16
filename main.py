from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

class Node:
    def __init__(self, value):
        self.value: int = value
        self.parent: Node = None
        self.children: Node = None
    
    
class LinkedList:
    def __init__(self):
        self.rootNode: Node = None 
        
    def print_linked_list(self):
        current = self.rootNode
        if current is None:
            print("Linked list is empty")
        else:
            while current is not None:
                print(current.value)
                current = current.parent 

    def insert(self, value):
        if self.rootNode is None:
            self.rootNode = Node(value) 
        else:
            current = self.rootNode
            while current.parent is not None:
                current = current.parent  
            current.parent = Node(value) 


linkedList = LinkedList()
linkedList.insert(5)
linkedList.insert(15)
linkedList.insert(0)

linkedList.print_linked_list()
        

htmlFile=""

with open("./main.html", 'r') as file:
    htmlFile = file.read()

@app.get('/')
async def root():
    return HTMLResponse(content=htmlFile)