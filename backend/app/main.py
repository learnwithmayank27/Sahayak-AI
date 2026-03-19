from fastapi import FastAPI
from app.api.routes import chat, health
from app.core.middleware import global_exception_handler

app = FastAPI(title="Shayak AI")

# Routes
app.include_router(chat.router, prefix="/api")
app.include_router(health.router, prefix="/api")

# Middleware
app.add_exception_handler(Exception, global_exception_handler)

@app.get("/")
def root():
    return {"message": "Shayak AI Backend Running"}
