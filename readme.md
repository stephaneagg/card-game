Frontend (React + Vite)

	Folder: frontend/

		Install dependencies:

			cd frontend
			npm install


		Run development server:

			npm run dev


	Available at: http://localhost:5173


	React structure suggestion:

src/
  components/
    Lobby.tsx
    GameTable.tsx
    PlayerList.tsx
  pages/
    Home.tsx
    Game.tsx
  App.tsx
  main.tsx


Notes:

Use fetch or axios to call backend REST APIs

Use WebSocket (native WebSocket or socket.io-client) for real-time updates

State management: useState for small state, Context or Redux for global game state


------------------------------------------------------------------------------------------------------------------------

Backend (FastAPI)

	Folder: backend/

	Install dependencies (use a Python venv):

		python -m venv venv
		source venv/bin/activate       # Linux / WSL
		# venv\Scripts\activate        # Windows
		pip install fastapi uvicorn


	Run backend server:

		uvicorn main:app --reload


	Available at: http://127.0.0.1:8000

------------------------------------------------------------------------------------------------------------------------

FastAPI structure suggestion:

backend/
  main.py        # entry point
  routes/
    lobby.py
    game.py
    users.py
  models/
    user.py
    game_state.py
  database.py


Notes:

Use @app.get / @app.post for REST endpoints

Use WebSocket for real-time gameplay (/ws)

Add CORS middleware to allow React dev server:

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
