from fastapi import FastAPI

app = FastAPI(title="Inventory API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return [{"id": 1, "name": "Widget", "quantity": 10}]