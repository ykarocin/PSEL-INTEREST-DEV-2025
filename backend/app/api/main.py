from fastapi import APIRouter

from app.api.routes import utils, users, teams, members

api_router = APIRouter()
api_router.include_router(utils.router)
api_router.include_router(users.router)
api_router.include_router(teams.router)
api_router.include_router(members.router)
