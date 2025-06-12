from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Wonders 🏔️"])


# Marvel Datas
@router.get("/wonders")
async def get_wonders():
    json_path = Path("database/wonders.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"wonders": data}