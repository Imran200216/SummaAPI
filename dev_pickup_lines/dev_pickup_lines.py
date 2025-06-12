from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Dev Pickup Lines 🧑🏻‍💻❤️"])


# Marvel Datas
@router.get("/developer_pickip_lines")
async def get_developer_pickup_lines():
    json_path = Path("database/developer_pickup_lines.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"developer_pickup_lines": data}