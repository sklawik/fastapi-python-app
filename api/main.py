from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return HTMLResponse(content="Welcome to FastAPI!", status_code=200)
router = APIRouter()