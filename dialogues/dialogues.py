from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Dialogues 🎭"])


# Marvel Datas
@router.get("/dialogues")
async def get_dialogues():
    json_path = Path("database/dialogues.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"dialogues": data}