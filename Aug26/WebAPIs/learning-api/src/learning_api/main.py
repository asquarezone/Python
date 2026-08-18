from fastapi import FastAPI

app = FastAPI(
    title="Learning API",
    description="API for learning purposes",
    version="0.0.1"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
