from fastapi import BackgroundTasks, APIRouter, Body, Request, Response, HTTPException, Query, Depends
from numpy.random import choice
from pydantic import EmailStr, BaseModel
from base.base_response import DataResponse
from helpers.enums import *
from models.reward import *
from database.query import *
import logging


logger = logging.getLogger(__name__)

router = APIRouter()

class FormData(BaseModel):
    secret_token: str


@router.post('', response_model=DataResponse[EReward]) #If data response is a class, change str to class
async def post(token_obj: FormData = Body(...)):
    token = token_obj.secret_token
    logger.info("test_random")
    res = choice([EReward.NONE, EReward.MONEY1, EReward.MONEY5, EReward.MONEY10, EReward.MONEY100, EReward.NETFLIX], size=None, replace=False, p=[0.1, 0, 0.2, 0.6, 0.1, 0]) #replace with probality in cofiguration
    #TODO: add to database with sercet token
    # print(form_data.dataString)
    # print(form_data.getdata_string)
    # print(res)
    if (res != EReward.NONE): 
        token_sample = Token(token=token, reward_type=res)
        res_token = await add_token_reward(token_sample)
        return DataResponse().success_response(res)
    return DataResponse().success_response(res)

