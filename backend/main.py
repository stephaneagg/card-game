from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    rank: int

# list of users
users = []

@app.get("/")
def root():
    return {"status": "backend running"}
    #return {"players": 1, "president": "player1", "bum": "player1"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI 🎉"}

@app.get("/api/lobby")
def players():
    return {"players": users}








# Allow React frontend access
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Only let your frontend connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
