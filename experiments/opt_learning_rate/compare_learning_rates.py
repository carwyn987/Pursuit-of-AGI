import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class NeuralNetworkModel(nn.Module):
    def __init__(self):
        super(NeuralNetworkModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # input and output dimensions are 1

    def forward(self, x):
        return self.linear(x)

    def train(self, dataset, epochs=100, custom_lr=False):
        torch.manual_seed(42)
        np.random.seed(42)

        criterion = nn.MSELoss()
        optimizer = optim.SGD(self.parameters(), lr=0.01)
        losses = []  # List to store the loss at each step
        for epoch in range(epochs):
            for i, (x, y) in enumerate(dataset):
                training_iteration = epoch * len(dataset) + i

                # print(x,y)

                if custom_lr:
                    # Set the learning rate for this sample
                    for param_group in optimizer.param_groups:
                        param_group['lr'] = 1.0 / (1.0 + training_iteration)

                x = x.float()  # Convert input to Float
                y = y.float()  # Convert label to Float
                optimizer.zero_grad()
                output = self.forward(x)
                loss = criterion(output, y)
                loss.backward()
                optimizer.step()
                losses.append(loss.item())  # Append the loss to the list

        return losses  # Return the list of losses

    def evaluate(self, dataset):

        torch.manual_seed(42)
        np.random.seed(42)

        criterion = nn.MSELoss()
        total_loss = 0
        with torch.no_grad():
            for x, y in dataset:
                x = x.float()  # Convert input to Float
                y = y.float()  # Convert label to Float
                output = self.forward(x)
                loss = criterion(output, y)
                total_loss += loss.item()
        return total_loss / len(dataset)

class SimpleDataset:
    def __init__(self, size=100):
        self.size = size
        self.data = np.random.rand(size, 1)
        self.labels = 2 * self.data + 1

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return torch.tensor(self.data[idx]), torch.tensor(self.labels[idx])

class ProbabilityDistributionDataset:
    def __init__(self, size, mean, std):
        self.size = size
        self.mean = mean
        self.std = std

        self.data = np.random.normal(self.mean, self.std, (size,1))
        self.labels = np.array([self.mean] * size).reshape(-1,1)

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return torch.tensor(self.data[idx], dtype=torch.float), torch.tensor(self.labels[idx], dtype=torch.float)

# Create two instances of the neural network model
model1 = NeuralNetworkModel()
model2 = NeuralNetworkModel()

# Create two instances of the simple dataset
dataset = SimpleDataset() # ProbabilityDistributionDataset(100,3.5,2.5) # Doesn't work well because it's a single parameter single input neural network, so it would be learning a bias and zero weight optimally

# Train the models on the datasets
l1s = model1.train(dataset, epochs=100, custom_lr=False)
l2s = model2.train(dataset, epochs=100, custom_lr=True)

# Evaluate the models on the datasets
loss1 = model1.evaluate(dataset)
loss2 = model2.evaluate(dataset)

print(f"Constant lr: {loss1}")
print(f"Theoretically Optimal lr: {loss2}")

import matplotlib.pyplot as plt
plt.plot(l1s, label='Constant lr')
plt.plot(l2s, label='Theoretically Optimal lr')
plt.legend()
plt.show()
