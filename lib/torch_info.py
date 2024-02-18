import torch


def torch_params_to_str(model):
    """
    Returns string containing all model parameters

    Restrictions:
     - Probably only works / is helpful on simple feed-forward networks
    """

    return_str = ""
    for name, param in model.named_parameters():
        return_str += f"    Layer: {name} | Size: {param.size()} | Values : {param[:2]}"

    return return_str
