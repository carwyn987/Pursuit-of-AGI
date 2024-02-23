import torch


class SingleLayerNNWithActivation(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.stack = torch.nn.Sequential(
            torch.nn.Linear(2, hidden_size, bias=True),
            torch.nn.ReLU(),
            torch.nn.Linear(hidden_size, 1, bias=True),
        )
        print(f"Model structure: {self}")

    def forward(self, x):
        return self.stack(x)
