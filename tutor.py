# src/backend/routers/tutor.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict

router = APIRouter(prefix="/tutor", tags=["Tutor"])

class ChatRequest(BaseModel):
    message: str
    student_id: int = None

class ChatResponse(BaseModel):
    response: str
    tips: Dict[str, str] = {}

# Placeholder tutoring endpoint.
# Replace the body with LLM API calls (OpenAI, local LLM) for real answers.
@router.post("/ask", response_model=ChatResponse)
def chat(request: ChatRequest):
    user_msg = request.message.strip().lower()

    # Very simple rule-based responses for prototype/demo
    if "explain" in user_msg or "what is" in user_msg or "define" in user_msg:
        resp = (
            "Here's a short explanation:\n\n"
            "This is a placeholder tutor response. In the full system, this endpoint "
            "will call an LLM (like OpenAI GPT) or an on-premise model to generate "
            "clear, step-by-step explanations tailored to the student."
        )
        tips = {"study_tip": "Try breaking the topic into small chunks and practice with quizzes."}
    elif "help" in user_msg or "struggl" in user_msg:
        resp = "It sounds like you need help. Try revisiting earlier topics or asking for examples."
        tips = {"next_step": "Request an easier explanation or specific example problems."}
    else:
        resp = f"I understood: '{request.message}'. (This is a demo response from the tutor API.)"
        tips = {}
    return ChatResponse(response=resp, tips=tips)
