from fastapi import FastAPI

app = FastAPI(
    title="Hello-api",
    summary="Learning FastAPI",
    version="0.0.1")

@app.get("/")
def home():
    return { "message": "hello" }

@app.get("/square/{number}")
def square(number: int):
    return {
        "result" : number ** 2
    }


@app.get("/cube/{number}")
def cube(number: int):
    return {
        "result": number ** 3
    }