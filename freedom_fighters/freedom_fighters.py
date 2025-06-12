from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Tamil Freedom Fighters 🤺"])


# Marvel Datas
@router.get("/freedom_fighters")
async def get_freedom_fighters():
    json_path = Path("database/freedom_fighters.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"wonders": data}