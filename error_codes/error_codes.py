from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Error Codes ❌"])


# Marvel Datas
@router.get("/tamil_proverbs")
async def get_error_codes():
    json_path = Path("database/error_codes.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"error_codes": data}