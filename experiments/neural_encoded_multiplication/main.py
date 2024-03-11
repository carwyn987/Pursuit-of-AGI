import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from tqdm import tqdm
import torch

torch.manual_seed(100)

from model import SingleLayerNNWithActivation
from multiplication_data_generator import multiplication_data_generator, CustDataset

if __name__ == "__main__":

    # Generate dataset (ds)
    train_tuple_list_ds = multiplication_data_generator(
        N=10, write=False, symmetric=True
    )
    test_tuple_list_ds = multiplication_data_generator(
        N=20, write=False, symmetric=True
    )

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
    model = SingleLayerNNWithActivation(100).to(device)
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters())

    training_loss_early_stopping_threshold = 0.1
    # training_loss_change_early_stopping_threshold = 5

    # Train loop
    loss_saves = []
    for j in (pbar := tqdm(range(epochs := 500))):
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

        if loss_saves[-1] < training_loss_early_stopping_threshold:
            break

        # If the average loss change is < training_loss_change_early_stopping_threshold, break
        # if len(loss_saves) > 10:
        #     first_difs = [y - x for x, y in zip(loss_saves[-11:-1], loss_saves[-10:])]
        #     if np.abs(np.mean(first_difs)) < training_loss_change_early_stopping_threshold:
        #         print(first_difs)
        #         break

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

    # Collect data for 3d plot
    inputs_error_plot_data = []
    for i, data in enumerate(test_dataloader):
        inputs, label = data
        y_pred = model(inputs.to(device)).to("cpu").detach().numpy()
        inputs_error_plot_data.append(
            (inputs[0][0].item(), inputs[0][1].item(), y_pred.item() - label.item())
        )

    x, y, z = [np.array(d) for d in zip(*inputs_error_plot_data)]
    colors = colors = cm.bwr(
        [
            0.99 if np.abs(x) <= 10 and np.abs(y) <= 10 else 0.01
            for x, y, z in inputs_error_plot_data
        ]
    )
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection="3d")
    ax.scatter(x, y, z, color=colors)
    ax.set_xlabel("Input 1")
    ax.set_ylabel("Input 2")
    ax.set_zlabel("Prediction Error")
    plt.title("Error Observed vs Input Data. Red Dots were trained on. Blue dots are test only.")

    plt.ion()
    plt.show(block=True)
