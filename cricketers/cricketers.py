from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Cricketers 🏏"])


# Marvel Datas
@router.get("/cricketers")
async def get_cricketers():
    json_path = Path("database/cricketers.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"cricketers": data}
