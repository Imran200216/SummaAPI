from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Nostalgic Cartoons ✨"])


# Marvel Datas
@router.get("/nostalgic_cartoons")
async def get_nostalgic_cartoons():
    json_path = Path("database/nostalgic_cartoons.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"toursim": data}