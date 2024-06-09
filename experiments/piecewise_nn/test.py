import torch
import torch.nn as nn

class CustomNeuralNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(CustomNeuralNetwork, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        x = self.fc(x)
        return x
    
def custom_loss_fn(y_pred, y_true):
    # Calculate the custom loss
    loss = torch.mean(torch.abs(y_pred - y_true))
    return loss

def instantiate_model_optimizer_loss(input_size, output_size):
    # Instantiate the custom neural network model
    model = CustomNeuralNetwork(input_size, output_size)
    
    # Instantiate the optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    # Instantiate the loss function
    loss_fn = nn.MSELoss()
    
    return model, optimizer, loss_fn

def train_step(model, optimizer, loss_fn, x, y):
    # Set the model to training mode
    model.train()
    
    # Zero the gradients
    optimizer.zero_grad()
    
    # Make predictions
    y_pred = model(x)
    
    # Calculate the loss
    loss = loss_fn(y_pred, y)
    
    # Backward pass
    loss.backward()
    
    # Update the weights
    optimizer.step()
    
    return loss.item()

def make_dataset(dropped_height):
    # Generate the input data
    x = torch.tensor(dropped_height).unsqueeze(1)
    
    G = 6.67430e-11  # m^3 kg^-1 s^-2
    M = 5.972e24  # kg
    R = 6.371e6  # m
    g = G * M / (R**2)
    
    air_resistance_factor = 0.5
    
    y = 0.5 * g * x**2 + dropped_height
    
    # Apply the air resistance
    y -= air_resistance_factor * g * x**2
    
    return x, y


def main():
    # Define the number of inputs and outputs
    input_size = 10
    output_size = 5

    # Create an instance of the custom neural network
    # model = CustomNeuralNetwork(input_size, output_size)

    # Print the model architecture
    # print(model)



if __name__ == "__main__":
    main()