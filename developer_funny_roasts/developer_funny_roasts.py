from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Developer Funny Roasts 🧑🏻‍💻😹"])


# Marvel Datas
@router.get("/developer_funny_roasts")
async def get_developer_funny_roasts():
    json_path = Path("database/developer_funny_roasts.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"developer_funny_roasts": data}
