import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI(
    title="Card game",
    description="a game played with cards",
    version="0.1.0"
  #  docs_url="/docs"
)

class Player(BaseModel):
    username: str

class Lobby(BaseModel):
    players: List[Player]
    winner: Player
    loser: Player

class RegisterReq():
    name: str

class LobbyReq():
    player_id: int
    lobby_id: int

## MEMORY ##
players = {}
lobbies={}
##

@app.get("/")
def root():
    return {"status": "backend running"}
    #return {"players": 1, "president": "player1", "bum": "player1"}

@app.post("/player/register")
def register_player(data: RegisterReq):
    player_id = str(uuid.uuid4())
    players[player_id] = {
        "name" : data.name
    }
    return {"player_id": player_id, "name:": RegisterReq.name}

@app.get("/players/")
def get_players():
    return players


@app.post("/lobby/create")
def create_lobby(data: LobbyReq):
    lobby_id = str(uuid.uuid4())
    lobbies[lobby_id] = {
        players: [data.player_id],
        "status": "waiting"
    }
    return {"lobby_id": lobby_id}

@app.get("/lobby/")
def list_lobbies():
    return lobbies

app.post("lobby/join")
def join_lobby(data: LobbyReq):
    # add lobby to lobby dict
    lobby = lobbies[data.lobby_id]

    # add player to lobby's list of players
    lobby["players"].append(data.player_id)

    if (len(lobby["players"]) > 6):
        lobby["status"] = "full"
    else:
        lobby["status"] = 6-len(lobby["players"]) + " spot(s) left"

    return {"lobby_id": data.lobby_id, "players": lobby["players", "status": ]}




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

