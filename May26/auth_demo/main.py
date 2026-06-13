from fastapi import FastAPI

app = FastAPI(title="fastapi authentication demo")

@app.get("/public")
def get_general_info():
    return {
        "title": "FastApi Authentication Demo",
        "description": "learning to build apis"
    }

@app.get("/me")
def get_profile():
    return {
        "name": "khaja",
        "email": "test@test.com",
        "mobile": "99999999999",
        "address": "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }

