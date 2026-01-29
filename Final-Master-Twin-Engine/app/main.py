from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Skill Intelligence Service",
    description="Master Twin Skill Evaluation Engine",
    version="1.0"
)

app.include_router(router)
