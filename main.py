from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()









@app.get('/bst')
async def root():
    
    numbers = {5, 4, 3, 2, 1}
    return {"data": [1,2,3,4,5]}


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
        raise HTTPException(status_code=404, detail="not found (item)")