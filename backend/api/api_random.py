from fastapi import BackgroundTasks, APIRouter, Body, Request, Response, HTTPException, Query, Depends
from numpy.random import choice
from pydantic import EmailStr, BaseModel
from base.base_response import DataResponse
from helpers.enums import *
from models.reward import *
from database.query import *
from helpers.exception_handler import *
from core.probability_reward import *
import logging
from typing import Generic, Type


logger = logging.getLogger(__name__)

router = APIRouter()

class FormData(BaseModel):
    secret_token: str


@router.post('/random', response_model=DataResponse[dict]) #If data response is a class, change str to class
async def post(token_obj: FormData = Body(...)):
    token = token_obj.secret_token 
    num_of_reward_token = await count_reward_token(token)
    if (num_of_reward_token >= numOfTurns):
        logger.info(f"{token}: out of turns")
        raise CustomException(http_code=400, code='400', message=str("Out of turns"))
    
    res = choice([EReward.NONE, EReward.MONEY1, EReward.MONEY5, EReward.MONEY10, EReward.MONEY100, EReward.NETFLIX], size=None, replace=False, p=[none, m1k, m5k, m10k, m100k, netflix]) #replace with probality in cofiguration
    #TODO: add to database with sercet token
    # print(form_data.dataString)
    # print(form_data.getdata_string)
    # print(res)


    token_sample = Token(token=token, reward_type=res)
    res_token = await add_token_reward(token_sample)
    logger.info(f"user: {token} got {res}")
    return DataResponse().success_response({"type_reward": res})

@router.get('/get-turn-left', response_model=DataResponse[dict])
async def getRemain(token: str):
    num_of_reward_token = await count_reward_token(token)
    return DataResponse().success_response(
        {"turn_left" : numOfTurns - num_of_reward_token})



