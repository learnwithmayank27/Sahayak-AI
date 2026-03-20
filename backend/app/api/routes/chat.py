from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import process_chat
from fastapi import Depends
from app.auth.dependencies import get_current_user

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

@router.post("/chat")
async def chat(req: ChatRequest, user=Depends(get_current_user)):
    return await process_chat(req.message, req.session_id)
