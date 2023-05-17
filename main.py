import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app import app
from app.routes.auth import user
from config import Config

app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app=app, host=Config.SERVER_HOST, port=Config.SERVER_PORT)
