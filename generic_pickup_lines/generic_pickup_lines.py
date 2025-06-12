from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Generic Pickup Lines 🥰"])


# Marvel Datas
@router.get("/generic_pickup_lines")
async def get_pickup_lines():
    json_path = Path("database/generic_pickup_lines.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"pickup_lines": data}