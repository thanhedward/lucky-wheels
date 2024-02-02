from fastapi import APIRouter

from api import api_random, get_reward_info, add_reward_people

router = APIRouter()


router.include_router(get_reward_info.router, tags=["reward"], prefix="/admin/reward")

router.include_router(api_random.router, tags=["user"], prefix="/user")

router.include_router(add_reward_people.router, tags = ["add-reward"], prefix="/admin/add_reward")
