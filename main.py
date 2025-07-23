from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root() -> dict: 
    return {"message": "Hello, World!"}

@app.get("/home")
async def read_home():
    return "Welcome to the home page!"