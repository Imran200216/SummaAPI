from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Emoji Quotes 😉"])


# Marvel Datas
@router.get("/emoji_quotes")
async def get_emoji_quotes():
    json_path = Path("database/emoji_quotes.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"emoji_quotes": data}