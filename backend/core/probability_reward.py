from helpers.enums import EReward
# change if reward has adjustment
# sum must be 1
netflix = 0.001 #0.1%
m100k = 0.002 #0.2%
m10k = 0.01 #1%
m5k = 0.02 #2%
m1k = 0.04 #4%
none = 0.927 #92.7%
max_config_obj = {
    EReward.NETFLIX: 1,
    EReward.MONEY100: 2,
    EReward.MONEY10: 2,
    EReward.MONEY5: 3,
    EReward.MONEY1: 5   
}

numOfTurns = 3