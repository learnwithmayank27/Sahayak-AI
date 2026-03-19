from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import process_chat

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

@router.post("/chat")
async def chat(req: ChatRequest):
    return await process_chat(req.message, req.session_id)
