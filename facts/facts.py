from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Facts 🝤"])


# Marvel Datas
@router.get("/facts")
async def get_facts():
    json_path = Path("database/facts.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"facts": data}
