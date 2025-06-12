from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Planets 🌎"])


# Marvel Datas
@router.get("/planet")
async def get_planets():
    json_path = Path("database/planets.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"planet": data}