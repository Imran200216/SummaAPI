from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Comedies 🤣"])


# Marvel Datas
@router.get("/comedy")
async def get_comedy():
    json_path = Path("database/comedy.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"comedy": data}
