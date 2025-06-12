from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["DC Comics 🦸🏻‍♂️"])


# Marvel Datas
@router.get("/dc")
async def get_dc_comics():
    json_path = Path("database/dc_comics.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"dc_comics": data}
