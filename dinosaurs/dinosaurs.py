from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Dinosaurs Species 🦖"])


# Marvel Datas
@router.get("/dinosaurs")
async def get_dinosaurs():
    json_path = Path("database/dinosaurs.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"dinosaurs": data}