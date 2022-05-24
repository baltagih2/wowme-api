import api.middleware
from api.config import app

# from api.routers import (
#     feedback,
#     hiscore,
#     label,
#     legacy,
#     legacy_debug,
#     player,
#     prediction,
#     report,
#     scraper,
# )

# app.include_router(hiscore.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Workout with Me API. If you're interested in becoming a developer, please contact ferrariictweet@gmail.com!"
    }


@app.get("/favicon")
async def favicon():
    return {}
