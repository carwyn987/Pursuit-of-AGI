import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import torch

torch.manual_seed(100)

from torch_dataset import CustDataset
from model import MinimalNeuralNetwork, NonminimalNeuralNetwork
from addition_data_generator import addition_data_generator

if __name__ == "__main__":

    # Generate dataset (ds)
    train_tuple_list_ds = addition_data_generator(N=100, write=False, symmetric=True)
    test_tuple_list_ds = addition_data_generator(N=200, write=False, symmetric=True)

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
    model = MinimalNeuralNetwork().to(device)
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # Train loop
    w_saves = []
    b_saves = []
    loss_saves = []
    for j in (pbar := tqdm(range(epochs := 50))):
        epoch_losses = []
        for data in train_dataloader:
            inputs, label = data
            y_pred = model(inputs.to(device)).to("cpu")
            loss = loss_fn(y_pred, label.unsqueeze(1))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_losses.append(loss.item())
        loss_saves.append(np.mean(epoch_losses))

        pbar.set_description(f"Current Loss: {loss.item()}")

        # Extract the current weights
        weights = list(model.parameters())[0].data.cpu().numpy().flatten()
        biases = list(model.parameters())[1].data.cpu().numpy().flatten()

        w_saves.append(tuple(weights))
        b_saves.append(tuple(biases))

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
    _, ax0 = plt.subplots()
    ax0.plot(list(range(len(loss_saves))), loss_saves, label="Average Epoch Loss")
    ax0.set_title("Average Epoch Loss vs Training Epoch")
    ax0.set_xlabel("Training Epoch")
    ax0.set_ylabel("Training Loss (MSE)")
    plt.legend()

    # Plot Training Parameters:
    _, ax1 = plt.subplots()
    # Plot **SOME** weights
    num_weights_biases_to_plot = 10  # each
    for n, weight_n in enumerate(zip(*w_saves)):
        if n < num_weights_biases_to_plot:
            ax1.plot(list(range(len(weight_n))), weight_n, label=f"Weight {n}")
    for n, bias_n in enumerate(zip(*b_saves)):
        if n < num_weights_biases_to_plot:
            ax1.plot(list(range(len(bias_n))), bias_n, label=f"Bias {n}")
    ax1.set_title("Model Parameters vs Training Epoch")
    ax1.set_xlabel("Training Epoch")
    ax1.set_ylabel("Model Parameter (Weights and Biases) Value")
    plt.legend()
    plt.show(block=True)
