# Thompson Sampling

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Thomson Sampling
import random
N = 10000 # количество пользователей
d = 10 # количество версий рекламы
ads_selected = [] # выбор рекламы на каждом шаге
numbers_of_rewards_1 = [0] * d # количество раз i реклама получила 1
numbers_of_rewards_0 = [0] * d # количество раз i реклама получила 0
total_reward = 0 # вознаграждение общее (сумма по всем рекламам)

for n in range(0, N) : # [0,10000)
  max_random = 0 # максимальная граница рекламы
  ad = 0 # индекс максимальной рекламы
  for i in range(0, d) :
    random_beta = random.betavariate(
        numbers_of_rewards_1[i] + 1, # почему + 1?
        numbers_of_rewards_0[i] + 1
      ) # получаем случайное число для i рекламы beta распределение

    if (random_beta > max_random) :
      max_random = random_beta
      ad = i


  ads_selected.append(ad) # выбранная реклама закидываем каждый шаг
  reward = dataset.values[n, ad] # получаем ответ от пользователя
  if reward == 1 : # считаем успешные отрабатывания рекламы
    numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
  else : # считаем негативные срабатывания рекламы
    numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1

  total_reward = total_reward + reward

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selectons (Thomson Sampling)')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
