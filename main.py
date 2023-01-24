from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def helloworld():
    return "Hello World"
