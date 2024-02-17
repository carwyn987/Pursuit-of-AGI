# Pursuit-of-AGI

This project aims to explore and push the current boundaries of Machine Learning (ML). It is and will further become both a directed results-driven effort, as well as a personal hobby. I also hope to establish a baseline and pointed research interest that will serve to benefit a future doctoral journey.

Implemented here is a bank of experiments, all regarding exploring the limits of current ML techniques, and neural generalization. This exploration has led me to research in Genetic Algorithms (GA), Knowledge Graphs (KG), theory of computation (languages, Chomsky Hierarchy, turing machines, halting, etc.), distributed/federated learning, neocortical theory, and much more.

## Installation

Generally, python 3.9 and torch 1.9.0 are used. Follow these steps to setup your environment:

1. Create a pip environment with Python 3.9 (assumes python3 refers to Python version 3.9)
```
/path/to/python3.9 -m venv p39
```
2. Activate the environment. You will need to activate the pip environment in each terminal in which you want to use this code.
```
source p39/bin/activate
```
3. Install the appropriate version of [PyTorch](https://pytorch.org/get-started/locally/). For me this looks like
```
pip3 install torch torchvision torchaudio
```
4. If prompted, upgrade pip (mine is 24.0), because "newer is better" 👍 
```
/path/to/python3.9 -m pip install --upgrade pip
```
5. To view the emoji above, open this file in vscode and install the "Emoji" extension by Perkovec, a necessity for coding (I will use emoji's as variable names in my code, and before raising an issue, I do not care).
4. Install the requirements:
```
pip3 install -r requirements.txt
```