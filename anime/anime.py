from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Anime 🐉"])


# Marvel Datas
@router.get("/anime")
async def get_planets():
    json_path = Path("database/anime.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"anime": data}