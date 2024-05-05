"""
Design and conduct an experiment to demonstrate the difficulties 
that sample-average methods have for nonstationary problems. Use 
a modified version of the 10-armed testbed in which all the q*(a) 
start out equal and then take independent random walks (say by 
adding a normally distriubted increment with mean 0 and standard 
deviation 0.01 to all the q*(a) samples)
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class Bandit:
    def __init__(self):
        self.mean = np.random.random()
        self.var = 1
        self.samples = []
        
    def sample(self):
        # Move mean
        self.mean + np.random.normal(0, 0.01)
        self.samples.append(np.random.normal(self.mean, self.var))
        return self.samples[-1]
    
    def get_sample_avg(self):
        return np.mean(self.samples) if len(self.samples) > 0 else 0
        
def interact(epsilon):

    total_max_reward = 0
    epochs = 100
    runs = 10000
    totaled_rewards = np.zeros((runs))

    for j in tqdm(range(epochs)):
        num_bandits = 10
        bandits = [Bandit() for _ in range(num_bandits)] # Bandit, sample average value

        actual_best_ind = max(range(len(bandits)), key=lambda i: bandits[i].mean)
        max_exp = bandits[actual_best_ind].mean
        optimal_choice_list = []

        
        for i in range(runs):
            # Get maximum q-value bandit, or the first equal one
            if np.random.random() < epsilon:
                action = int(np.random.random()*num_bandits)
            else:
                action = max(range(len(bandits)), key=lambda i: bandits[i].get_sample_avg())

            # Take action
            reward = bandits[action].sample()
            optimal_choice_list.append(reward)

        total_max_reward += max_exp
        totaled_rewards += np.array(optimal_choice_list)

    totaled_rewards /= total_max_reward
    optimal_choice_list = list(totaled_rewards)

    # PLOT
    # cdf_ba = []
    cdf_ba_e = []
    summ = sum(optimal_choice_list[0:100])
    for i in range(len(optimal_choice_list)-100):
        cdf_ba_e.append(summ/(100*max_exp))
        summ -= optimal_choice_list[i]
        summ += optimal_choice_list[i+100]
        # cdf_ba.append(sum(optimal_choice_list[i:i+100])/(100*max_exp))
    return cdf_ba_e

if __name__ == "__main__":
    
    from scipy.ndimage import gaussian_filter1d
    ks = 100 # kernal size
    fn = lambda x,y: x
    # fn = gaussian_filter1d
    epsilon0 = y3 = fn(interact(0), ks)
    epsilon1 = fn(interact(1), ks)
    epsilon0_1 = fn(interact(0.1), ks)
    epsilon0_01 = fn(interact(0.01), ks)
    
    plt.plot(epsilon0, c="black", label="Epsilon=0, completely greedy")
    plt.plot(epsilon1, c="red", label="Epsilon=1, completely random")
    plt.plot(epsilon0_1, c="orange", label="Epsilon=0.1")
    plt.plot(epsilon0_01,c="gray", label="Epsilon=0.01")
    plt.legend()
    plt.show()