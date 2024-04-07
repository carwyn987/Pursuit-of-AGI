import torch
import numpy as np
from tqdm import tqdm
from torchsummary import summary

# Define data : a sequence of integers increasing linearly by 1

input_size = 100
compressed_size = 50

train_data = np.zeros((200,100))
for i in range(train_data.shape[0]):
    rand_int = int(np.random.random()*100)
    train_data[i,:] = np.arange(rand_int, rand_int + 100, 1)
    
test_data = np.zeros((400,100))
for i in range(test_data.shape[0]):
    rand_int = int(np.random.random()*200)
    test_data[i,:] = np.arange(rand_int, rand_int + 100, 1)


# Define model + optimizer + loss
class LinearAutoEncoder(torch.nn.Module):
    def __init__(self, input_size, compressed_size):
        super().__init__()
        self.network = torch.nn.Sequential(
            torch.nn.Linear(input_size, (input_size + compressed_size)//2),
            torch.nn.ReLU(),
            torch.nn.Linear((input_size + compressed_size)//2, compressed_size),
            torch.nn.ReLU(),
            torch.nn.Linear(compressed_size, (input_size + compressed_size)//2),
            torch.nn.ReLU(),
            torch.nn.Linear((input_size + compressed_size)//2, input_size),
        )

    def forward(self, input):
        return self.network(input)

nn = LinearAutoEncoder(input_size, compressed_size)
lossFunc = torch.nn.MSELoss()
optimizer = torch.optim.Adam(nn.parameters())

# summary(nn, input_size=(1, 100))

# Train
loss_saves = []

for i in tqdm(range(2077)):
    train_data_tensor = torch.tensor(train_data, dtype=torch.float32)  # Convert to torch tensor with float32 dtype
    out = nn(train_data_tensor)
    loss = lossFunc(out, train_data_tensor)
    loss_saves.append(loss.item())

    # zero the gradients accumulated from the previous steps,
    # perform backpropagation, and update model parameters
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # print(loss.item())

    if np.mean(loss_saves) < 1e-1:
        print("Training has converged!")
    

import matplotlib.pyplot as plt
plt.plot(range(len(loss_saves)), loss_saves)

# Test
test_losses = []
for i in range(test_data.shape[0]):
    test_data_tensor = torch.tensor(test_data[i,:], dtype=torch.float32)  # Convert to torch tensor with float32 dtype
    out = nn(test_data_tensor)
    loss = lossFunc(out, test_data_tensor)
    print("Input: ", test_data[i,0:5], ", Output: ", out.detach().numpy()[0:5])
    test_losses.append(loss.item())


plt.plot(range(len(test_losses)), test_losses)

# Compute mean of MSE's

mmse = np.mean(test_losses)
error = np.sqrt(mmse * 100)/100
print("Average item (100 items / sample) error: ", error)

plt.show()