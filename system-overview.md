# System Overview - EduMind (Prototype)

## Goal
EduMind provides personalized learning for students by:
- Generating quizzes
- Providing an AI tutor interface
- Tracking student performance (sample CSV provided)

## Backend
- FastAPI service running on `main.py`
- Routers:
  - `/quiz/generate` — returns a generated quiz (placeholder logic)
  - `/tutor/ask` — returns tutor-style responses (placeholder logic)
  - `/health/ping` — health check

## How to run locally
1. `cd src/backend`
2. `pip install -r requirements.txt`
3. `uvicorn main:app --reload --port 8000`
4. Visit `http://127.0.0.1:8000/docs` for interactive API docs.

## Next steps (recommended)
- Replace placeholder quiz generation with an LLM call (OpenAI or local)
- Implement user authentication and persistence (database)
- Add endpoints to submit quiz results and update user profiles
- Implement risk-prediction model and admin analytics dashboard
