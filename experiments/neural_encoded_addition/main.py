import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import torch

torch.manual_seed(100)

from torch_dataset import CustDataset
from model import NeuralNetwork
from addition_data_generator import addition_data_generator

if __name__ == "__main__":

    # Generate dataset (ds)
    train_tuple_list_ds = addition_data_generator(N=10, write=False, symmetric=True)
    test_tuple_list_ds = addition_data_generator(N=20, write=False, symmetric=True)

    train_dataset = CustDataset(*zip(*train_tuple_list_ds))
    test_dataset = CustDataset(*zip(*test_tuple_list_ds))

    train_dataloader = torch.utils.data.DataLoader(
        train_dataset, batch_size=10, shuffle=True
    )
    test_dataloader = torch.utils.data.DataLoader(
        test_dataset, batch_size=1, shuffle=False
    )  # requires batch_size=1

    # Select GPU
    device = (
        "cuda"
        if torch.cuda.is_available()
        else "mps" if torch.backends.mps.is_available() else "cpu"
    )
    print(f"Using {device} device")

    # Define model, optimizer, and loss
    model = NeuralNetwork().to(device)
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # Train loop
    w_saves = []
    b_saves = []
    for j in (pbar := tqdm(range(epochs := 200))):
        for data in train_dataloader:
            inputs, label = data
            y_pred = model(inputs.to(device)).to("cpu")
            loss = loss_fn(y_pred, label.unsqueeze(1))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        pbar.set_description(f"Current Loss: {loss.item()}")

        # Extract the current weights
        weights = list(model.parameters())[0].data.cpu().numpy()[0]
        bias = list(model.parameters())[1].data.cpu().numpy()[0]

        w_saves.append(tuple(weights))
        b_saves.append(bias)

    # Evaluation - First, print final model parameters
    print("Final Model Parameters:")
    for name, param in model.named_parameters():
        print(f"    Layer: {name} | Size: {param.size()} | Values : {param[:2]}")

    # Test RMSE
    rmse = 0
    for i, data in enumerate(test_dataloader):
        inputs, label = data
        y_pred = model(inputs.to(device)).to("cpu").detach().numpy()
        rmse += (y_pred.item() - label.item()) ** 2
    rmse = (rmse / len(test_dataloader)) ** 0.5
    print(f"RMSE of test data is {rmse:.4f}")

    # Plot Training Loss:
    w1, w2 = zip(*w_saves)
    fig, ax = plt.subplots()
    ax.plot(list(range(len(w_saves))), w1, label="Weight 1")
    ax.plot(list(range(len(w_saves))), w2, label="Weight 2")
    ax.plot(list(range(len(w_saves))), b_saves, label="Bias")
    ax.set_title("Model Parameters vs Training Epoch")
    ax.set_xlabel("Training Epoch")
    ax.set_ylabel("Model Parameter (Weights and Biases) Value")
    plt.legend()
    plt.show(block=True)
