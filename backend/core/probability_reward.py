from helpers.enums import EReward
# change if reward has adjustment
# sum must be 1
netflix = 0 #0%
m100k = 0.015 #1.5%
m10k = 0.1 #10%
m5k = 0.055 #5.5%
m1k = 0.2 #20%
none = 0.63 #63%
max_config_obj = {
    EReward.NETFLIX: 0,
    EReward.MONEY100: 2,
    EReward.MONEY10: 7,
    EReward.MONEY5: 5,
    EReward.MONEY1: 5   
}

numOfTurns = 3