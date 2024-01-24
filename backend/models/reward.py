from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel
from helpers.enums import EReward

class Reward(Document):
    banking_number: str
    bank: str
    name: str
    secret_token: str
    reward_type: EReward
    money_tranfered: bool

    class Config:
        json_schema_extra = {
            "example": {
                "banking_number": "1800 588 822",
                "bank": "BIDV",
                "name": "Vu Manh Tien",
                "secret_token": "123awfw34m2",
                "reward_type": EReward.NONE,
                "money_tranfered": False
            }
        }
    
    class Settings:
        name="reward"