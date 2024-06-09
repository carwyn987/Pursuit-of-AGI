import numpy as np
import matplotlib.pyplot as plt

# Each "armed bandit" has a unique and unknown probability distribution governing its actions.

num_bandits = 10
samples = 100

# For each bandit, choose a distribution, mean and variance
bandit_samples = np.random.normal(np.random.random(num_bandits)*0.5 + 0.25, np.random.random(num_bandits)*0.2, size=(samples, num_bandits))

# Now we should have 100x10
# for i in range(num_bandits):
#     plt.plot(np.ones((samples,)) *  i,bandit_samples[:,i])

fig, ax = plt.subplots(figsize=(14,10))
plt.title("Multi-Armed Bandit")
ax.set_xlabel("Arm")
ax.set_ylabel("Observed Samples?")
plt.violinplot(bandit_samples)
plt.show()