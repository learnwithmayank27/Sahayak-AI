from fastapi import FastAPI
from app.api.routes import chat, health
from app.api.routes.auth import auth_routes
from app.core.middleware import global_exception_handler
from app.db.sql.database import Base, engine
from app.db.qdrant_client import init_collection

# ✅ CREATE APP FIRST
app = FastAPI(title="Shayak AI")

# ✅ STARTUP EVENT (DB INIT)
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    init_collection()

# ✅ ROUTES
app.include_router(chat.router, prefix="/api")
app.include_router(health.router, prefix="/api")
app.include_router(auth_routes.router, prefix="/api/auth")

# ✅ ERROR HANDLER
app.add_exception_handler(Exception, global_exception_handler)

@app.get("/")
def root():
    return {"message": "Shayak AI Backend Running"}
