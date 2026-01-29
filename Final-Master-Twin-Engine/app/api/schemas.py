from pydantic import BaseModel
from typing import List

class MotionInput(BaseModel):
    trajectory: List[List[float]]
    timestamps: List[float]
    collisions: List[bool]

class SkillOutput(BaseModel):
    score: int
    phase: str
    hint: str
