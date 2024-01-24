from helpers.enums import EReward
# change if reward has adjustment
# sum must be 1
netflix = 0.002 #0.2%
m100k = 0.001 #0.1%
m10k = 0.01 #0%
m5k = 0.02 #2%
m1k = 0.04 #4%
none = 0.927 #92.7%
max_config_obj = {
    EReward.NETFLIX: 2,
    EReward.MONEY100: 2,
    EReward.MONEY10: 5,
    EReward.MONEY5: 2,
    EReward.MONEY1: 2
}