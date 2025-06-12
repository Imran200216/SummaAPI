from fastapi import FastAPI
from marvel.marvel import router as marvel_router
from planet.planet import router as planet_router
from anime.anime import router as anime_router
from tourism.tourism import router as tourism_router
from wonders.wonders import router as wonder_router
from dinosaurs.dinosaurs import router as dinosaurs_router
from comedy.comedy import router as comedy_router
from dialogues.dialogues import router as dialogue_router
from freedom_fighters.freedom_fighters import router as freedom_fighters_router
from cartoons.nostalgic_cartoons import router as nostalgic_cartoons_router
from dc_comics.dc_comics import router as dc_comics_router
from facts.facts import router as facts_router
from tamil_proverbs.tamil_proverbs import router as tamil_proverbs_router
from error_codes.error_codes import router as error_codes_router
from generic_pickup_lines.generic_pickup_lines import (
    router as generic_pickup_lines_router,
)
from emoji_quotes.emoji_quotes import router as emoji_quotes_router
from dev_pickup_lines.dev_pickup_lines import router as developer_pickup_lines_router
from developer_funny_roasts.developer_funny_roasts import (
    router as developer_funny_roasts_router,
)


app = FastAPI(title="SummaAPI 👽💥")


# Routers
app.include_router(marvel_router)
app.include_router(planet_router)
app.include_router(anime_router)
app.include_router(tourism_router)
app.include_router(wonder_router)
app.include_router(dinosaurs_router)
app.include_router(comedy_router)
app.include_router(dialogue_router)
app.include_router(freedom_fighters_router)
app.include_router(nostalgic_cartoons_router)
app.include_router(dc_comics_router)
app.include_router(facts_router)
app.include_router(tamil_proverbs_router)
app.include_router(error_codes_router)
app.include_router(generic_pickup_lines_router)
app.include_router(emoji_quotes_router)
app.include_router(developer_pickup_lines_router)
app.include_router(developer_funny_roasts_router)
