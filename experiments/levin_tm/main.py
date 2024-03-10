"""

"""

from levin_tm_module.context_manager import ContextManager
from levin_tm_module.dataset_generators.generators import generate_ones
from levin_tm_module.losses.mse import index_match_MSE

if __name__ == "__main__":
    
    # Set up data
    inputs = []
    labels = generate_ones(100)

    # Set up context manager
    stopping_cond = lambda a,b: True if a < 0 else False
    cm = ContextManager(inputs, labels, fitness_fn=index_match_MSE, stopping_cond=stopping_cond, max_steps=1000)

    # Main loop
    best_tm, fitness, status = cm.run()
    