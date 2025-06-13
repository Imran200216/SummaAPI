from fastapi import FastAPI, APIRouter
import json
from pathlib import Path

router = APIRouter(tags=["Books 📚"])


# Marvel Datas
@router.get("/books")
async def get_books():
    json_path = Path("database/books.json")
    with open(json_path, "r") as f:
        data = json.load(f)
    return {"books": data}