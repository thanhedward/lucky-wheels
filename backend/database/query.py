from typing import List, Union

from beanie import PydanticObjectId

from models.reward import Reward
from models.token import Token

from helpers.enums import EReward

reward_collection = Reward
token_collection = Token

async def add_token_reward(new_token: Token) -> Token:
    token = await new_token.create()
    return token


async def find_token(token: str) -> List[Token]:
    token_rewards = await token_collection.find({"token": token}).to_list()
    return token_rewards

async def add_reward(new_reward: Reward) -> Reward:
    reward = await new_reward.create()
    return reward


async def retrieve_rewards() -> List[Reward]:
    rewards = await reward_collection.all().to_list()
    return rewards

async def retrieve_single_reward(id: PydanticObjectId) -> Reward:
    reward = await reward_collection.get(id)
    if reward:
        return reward
    
async def retrieve_single_type(type_reward: EReward) -> List[Reward]:
    reward_filter_type = await reward_collection.find({"reward_type": type_reward}).to_list()
    return reward_filter_type

async def count_single_type(type_reward: EReward) -> int:
    num_reward_by_type = await reward_collection.find({"reward_type": type_reward}).count()
    return num_reward_by_type

async def delete_reward(id: PydanticObjectId) -> bool:
    reward = await reward_collection.get(id)
    if reward:
        await reward.delete()
        return True
    

async def update_tranfered_status(id: PydanticObjectId) -> Union[bool, Reward]: #can return boolean or reward object
    update_query = {"$set": {"money_tranfered": True}}
    reward = await reward_collection.get(id)
    if reward:
        await reward.update(update_query)
        return reward
    return False