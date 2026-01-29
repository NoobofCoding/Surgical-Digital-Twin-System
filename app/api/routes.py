from fastapi import APIRouter
from app.api.schemas import MotionInput, SkillOutput
from app.services.evaluator import evaluate_motion
from app.utils.loader import load_expert

router = APIRouter()

expert_data = load_expert("app/data/expert/suturing.json")

@router.post("/evaluate", response_model=SkillOutput)
def evaluate(input: MotionInput):
    result = evaluate_motion(input.dict(), expert_data)
    return result
