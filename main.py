from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.rootNode = None 
        
    def insert(self, value):
        if self.rootNode is None:
            self.rootNode = Node(value)  
        else:
            self._insert(self.rootNode, value)  
    def _insert(self, node: Node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    def search(self, node: Node, _value: int) -> bool:
        currentNode: Node = node
        if currentNode is None:
            return False 
        if currentNode.value == _value:
            return True  
        return self.search(currentNode.left, _value) or self.search(currentNode.right, _value)
            
            
    def print_tree(self, node):
        if node:
            self.print_tree(node.left)
            print(node.value)
            self.print_tree(node.right)
            

    def min_value(self, currentNode: Node)->Node:
        if currentNode == None:
            currentNode = self.rootNode
        if currentNode.left is not None:
            return self.min_value(currentNode.left)
        else:
            return currentNode
    def max_value(self, currentNode: Node)->Node:
        if currentNode == None:
            currentNode = self.rootNode
        if currentNode.right is not None:
            return self.max_value(currentNode.right)
        else:
            return currentNode
     
    def delete(self, root: Node, value: int) -> Node:
        if root is None:
            return root
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_value_node = self.min_value(root.right)
            root.value = min_value_node.value  

            root.right = self.delete(root.right, min_value_node.value)

        return root
        

tree = BST()
tree.insert(5)
tree.insert(10)
tree.insert(-1)
tree.insert(6)
tree.insert(-50)
tree.insert(300)

# czy istnieje 4 - False
print(tree.search( tree.rootNode,4))
# czy istnieje -50 True
print(tree.search( tree.rootNode,-50))
tree.print_tree(tree.rootNode)
        
print("najmniejsza wartosc: ",tree.min_value(tree.rootNode).value)
print("najwieksza wartosc: ",tree.max_value(tree.rootNode).value)

tree.delete(tree.rootNode, 300)
tree.print_tree(tree.rootNode)

print("wartosc 300 zostalo usuniete")

# strona html serwowana domyślnie
@app.get('/')
async def root():
    with open("./main.html", 'r') as file:
        htmlFile = file.read()
    return HTMLResponse(content=htmlFile)

items = []

@app.get("/items")
def create_item(item: str):
    items.append(item)
    return items.__len__()


@app.get("/items/{item_id}")
def get_item(item_id: int)->str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="brak")