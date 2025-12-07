from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "backend running"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI 🎉"}
