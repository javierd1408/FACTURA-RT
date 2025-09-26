from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text   # <-- agrega esto
import socketio
from .db import init_db
from .deps import get_db

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
asgi_app = socketio.ASGIApp(sio)

app = FastAPI(title="Factura RT – Demo Pública")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    try:
        init_db()
    except Exception as e:
        # No abortar la app por DB no lista
        print("DB not ready yet (continuing):", e)

@app.get("/api/health")
def health(db=Depends(get_db)):
    db.execute(text("SELECT 1"))   # <-- usa text(...)
    return {"status": "ok"}

# Eventos demo
@sio.event
async def connect(sid, environ):
    await sio.save_session(sid, {"user": "anon"})
    await sio.emit("presence", {"msg": "user-connected", "sid": sid})

@sio.event
async def disconnect(sid):
    await sio.emit("presence", {"msg": "user-disconnected", "sid": sid})

# Montar websockets
app.mount("/rt", asgi_app)

