import torch


class MinimalNeuralNetwork(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.stack = torch.nn.Sequential(torch.nn.Linear(2, 1, bias=True))
        print(f"Model structure: {self}")

    def forward(self, x):
        return self.stack(x)


class NonminimalNeuralNetwork(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.stack = torch.nn.Sequential(
            torch.nn.Linear(2, 100, bias=True), torch.nn.Linear(100, 1, bias=True)
        )
        print(f"Model structure: {self}")

    def forward(self, x):
        return self.stack(x)
