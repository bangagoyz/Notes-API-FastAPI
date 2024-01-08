from fastapi import FastAPI
from router.route import routerr

app = FastAPI()

app.include_router(routerr)

@app.get('/')
async def Home():
    return "WELCOME HOME"
