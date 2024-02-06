from fastapi import BackgroundTasks, APIRouter, Body, Request, Response, HTTPException, Query, Depends
import logging
from pydantic import EmailStr, BaseModel
from base.base_response import DataResponse
from database.query import *
from models.reward import *
from core.probability_reward import *
from core.config import update_probability
logger = logging.getLogger(__name__)

router = APIRouter()

class AddRewardDto(BaseModel):
    banking_number: str
    bank: str
    name: str
    secret_token: str
    type_reward: EReward

@router.post('', response_model=DataResponse[str]) #If data response is a class, change str to class
async def add_reward_by_type(reward_dto: AddRewardDto = Body(...)):
    # new_reward = await add_reward(reward)
    # reward.reward_type = type_reward
    token_reward = await find_token(reward_dto.secret_token)
    fake_token = False
    for reward in token_reward:
        if reward.reward_type == reward_dto.type_reward:
            fake_token = True

    if not fake_token:
        return DataResponse().success_response("Token and reward don't match!")

    new_reward = Reward(
        banking_number=reward_dto.banking_number,
        bank=reward_dto.bank,
        name=reward_dto.name,
        secret_token=reward_dto.secret_token,
        reward_type=reward_dto.type_reward,
        money_tranfered=False
    )

    res_add_reward = await add_reward(new_reward)
    
    count = await count_single_type(reward_dto.type_reward)
    if (count == max_config_obj[reward_dto.type_reward]):
        new_probality = 0
        if (reward_dto.type_reward == EReward.NETFLIX):
            new_probality = netflix + none
        elif (reward_dto.type_reward == EReward.MONEY100):
            new_probality = m100k + none
        elif (reward_dto.type_reward == EReward.MONEY10):
            new_probality = m10k + none
        elif (reward_dto.type_reward == EReward.MONEY5):
            new_probality = m5k + none
        elif (reward_dto.type_reward == EReward.MONEY1):
            new_probality = m1k + none
        elif (reward_dto.type_reward == EReward.NONE):
            return HTTPException(status_code=400, detail=str("Input type reward not valid"))
        try:
            res_update_zero = update_probability(reward_dto.type_reward.value, 0)
            res_update_none_reward = update_probability(EReward.NONE.value, new_probality)
            if not res_update_zero or not res_update_none_reward:
                return DataResponse().success_response("Reward not found in database")
        except Exception as e:
            return HTTPException(status_code=400, detail=str(e))
    
    # print(form_data.dataString)
    # print(form_data.getdata_string)
    return DataResponse().success_response("Add reward to database successfully")




