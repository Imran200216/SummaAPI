from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Tourism 🛕"])


# Marvel Datas
@router.get("/tourism")
async def get_tourism():
    json_path = Path("database/tourism.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"toursim": data}