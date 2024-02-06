from fastapi import BackgroundTasks, APIRouter, Body, Request, Response, HTTPException, Query, Depends
import logging
from pydantic import EmailStr, BaseModel
from base.base_response import DataResponse
from database.query import *
from models.reward import *

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/{token}", response_model=DataResponse[str])
async def tranfer_money(token: str):
    query_status = await delete_reward(token)
    if query_status:
        return DataResponse().success_response("Deleted all tokens successfully")
    else: 
        return DataResponse().custom_response("1", "Failed", "Check token again!")
