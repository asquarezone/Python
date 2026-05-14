from fastapi import FastAPI
import asyncio

# Main application object
# which uvicorn should know about
app = FastAPI(
    title="hello-fast-api",
    description="A simple hello world app built with FastAPI",
)


@app.get("/customers")
async def list_customers():
    await asyncio.sleep(1)
    return [{"name": "John"}, {"name": "Jane"}]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=18800)

