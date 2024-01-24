from fastapi import BackgroundTasks, APIRouter, Body, Request, Response, HTTPException, Query, Depends
import logging
from pydantic import EmailStr, BaseModel
from base.base_response import DataResponse
from database.query import *
from models.reward import *

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/get-all-reward", response_description="Reward retrieved", response_model=DataResponse[List])
async def get_all_reward():
    rewards = await retrieve_rewards()
    return DataResponse().success_response(rewards)

@router.get("/filter-reward-type/{reward_type}", response_description="Reward type retrieved", response_model=DataResponse[List])
async def filter_reward(reward_type: str):
    logger.info(reward_type)
    rewards_filtered = await retrieve_single_type(reward_type)
    return DataResponse().success_response(rewards_filtered)

@router.get("/tranfer-money/{id}", response_model=Union[DataResponse[str], DataResponse[Reward]])
async def tranfer_money(id: PydanticObjectId):
    reward = await update_tranfered_status(id)
    if reward:
        print(type(reward))
        print(reward)
        return DataResponse().success_response(reward)
    return DataResponse().success_response("Update failed, check your id again!")

