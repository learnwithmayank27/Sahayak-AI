from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import process_chat

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(req: ChatRequest):
    response = await process_chat(req.message)
    return response
