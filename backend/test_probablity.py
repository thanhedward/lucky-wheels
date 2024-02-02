from core.config import update_probability
from helpers.enums import EReward
from numpy.random import choice
from collections import Counter
import matplotlib.pyplot as plt 
from core.probability_reward import *

# try:
#     update_probability("none_reward", 0.96)
# except ValueError as ve:
#     print(ve)

sample_arr = []

def random_reward():
    return choice([EReward.NONE.value, EReward.MONEY1.value, EReward.MONEY5.value, EReward.MONEY10.value, EReward.MONEY100.value, EReward.NETFLIX.value], size=None, replace=False, p=[none, m1k, m5k, m10k, m100k, netflix])


for i in range(0, 100):
    sample_arr.append(random_reward())

element_counts = Counter(sample_arr)

# print(element_counts)

plt.bar(element_counts.keys(), element_counts.values(), align='center', alpha=0.7)
plt.xlabel('Phần tử')
plt.ylabel('Số lần xuất hiện')
plt.title('Xác suất')
plt.show()

# print(sample_arr)