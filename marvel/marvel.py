from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Marvel 🕷️"])


# Marvel Datas
@router.get("/marvel")
async def get_marvels():
    json_path = Path("database/marvel.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"marvel": data}
