from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel
from helpers.enums import EReward

class   Token(Document):
    token: str
    reward_type: EReward

    class Config:
        json_schema_extra = {
            "example": {
                "token": "2oij24k3l4",
                "reward_type": EReward.MONEY10
            }
        }
    
    class Settings:
        name="token"