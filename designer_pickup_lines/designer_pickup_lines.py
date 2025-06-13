from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Designer Pickup Lines 👨🏻‍🎨❤️"])


# Marvel Datas
@router.get("/designer_pickip_lines")
async def get_designer_pickup_lines():
    json_path = Path("database/designer_pickup_lines.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"designer_pickup_lines": data}