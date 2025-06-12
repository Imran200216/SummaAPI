from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Tamil Proverbs அ"])


# Marvel Datas
@router.get("/tamil_proverbs")
async def get_wonders():
    json_path = Path("database/tamil_proverbs.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"tamil_proverbs": data}