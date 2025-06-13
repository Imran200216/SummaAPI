from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Tamil Proverbs அ"]) 

@router.get("/tamil_proverbs")
async def get_tamil_proverbs():
    try:
        json_path = Path("database/tamil_proverbs.json")
        if not json_path.exists():
            return {"error": "JSON file not found"}

        with open(json_path, "r") as f:
            data = json.load(f)
        return {"tamil_proverbs": data}

    except Exception as e:
        return {"error": str(e)}
