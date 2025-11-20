# src/backend/routers/quiz.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import uuid

router = APIRouter(prefix="/quiz", tags=["Quiz"])

class QuizRequest(BaseModel):
    topic: str
    difficulty: str = "medium"   # easy / medium / hard
    num_questions: int = 5

class Question(BaseModel):
    id: str
    question: str
    options: List[str] = []
    answer: str = ""   # In production don't return the answer to clients!

class QuizResponse(BaseModel):
    quiz_id: str
    topic: str
    difficulty: str
    questions: List[Question]

# Simple placeholder generator (replace with LLM calls)
SAMPLE_QUESTIONS = {
    "math": [
        ("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
        ("What is 3 * 5?", ["8", "15", "20", "10"], "15"),
        ("What is 10 / 2?", ["2", "5", "10", "8"], "5"),
    ],
    "science": [
        ("What planet is known as the Red Planet?", ["Earth","Mars","Jupiter","Venus"], "Mars"),
        ("What is H2O commonly called?", ["Salt", "Water", "Oxygen", "Hydrogen"], "Water"),
    ],
    "english": [
        ("Choose the correctly spelled word.", ["Recieve","Receive","Recive","Receeve"], "Receive"),
        ("What is a synonym for 'happy'?", ["Sad","Elated","Angry","Tired"], "Elated"),
    ],
}

@router.post("/generate", response_model=QuizResponse)
def generate_quiz(req: QuizRequest):
    topic_key = req.topic.strip().lower()
    # Use LLM/templating here; this is a deterministic placeholder.
    sample_list = SAMPLE_QUESTIONS.get(topic_key, [])
    if not sample_list:
        # Fallback: create simple arithmetic questions for unknown topics
        sample_list = [
            ("What is 1 + 1?", ["1", "2", "3", "4"], "2"),
            ("What is 5 - 2?", ["1", "2", "3", "4"], "3"),
            ("What is 4 * 2?", ["6", "7", "8", "9"], "8"),
        ]
    questions = []
    for i in range(min(req.num_questions, len(sample_list))):
        q_text, opts, ans = sample_list[i]
        questions.append(Question(
            id=str(uuid.uuid4()),
            question=q_text,
            options=opts,
            answer=ans
        ))
    # If requested more than sample set, repeat or generate placeholders
    while len(questions) < req.num_questions:
        questions.append(Question(
            id=str(uuid.uuid4()),
            question=f"Synthetic question {len(questions)+1} on {req.topic}",
            options=["A","B","C","D"],
            answer="A"
        ))
    return QuizResponse(
        quiz_id=str(uuid.uuid4()),
        topic=req.topic,
        difficulty=req.difficulty,
        questions=questions
    )
