import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import models as models
from typing import List

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
load_dotenv(os.path.join(BASE_DIR, '.env'))


class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'FASTAPI')
    # SECRET_KEY = os.getenv('SECRET_KEY', '')
    API_PREFIX: str  = ''
    BACKEND_CORS_ORIGINS: List[str] = ['*']
    DATABASE_URL: str = os.getenv('DATABASE_URL', '')
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECURITY_ALGORITHM: str = 'HS256'
    LOGGING_CONFIG_FILE: str = os.path.join(BASE_DIR, 'log_conf.yaml')


settings = Settings()


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(), document_models=models.__all__
    )


# try catch exception
def update_probability(reward, weight):
    updated = False
    url_config_file = f'{BASE_DIR}/core/probability_reward.py'
    with open(url_config_file, 'r') as file:
        config_probability = file.readlines()
    for i in range(len(config_probability)):
        if reward in config_probability[i]:
            updated = True
            config_probability[i] = f'{reward} = {weight} #{weight * 100}%\n'
    with open(url_config_file, 'w') as file:
        file.writelines(config_probability)
    if updated:
        return True
    else:
        return False