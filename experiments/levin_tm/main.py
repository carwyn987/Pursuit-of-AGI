"""

"""

import random
import copy

from levin_tm_module.context_manager import ContextManager
from levin_tm_module.dataset_generators.generators import generate_ones
from levin_tm_module.losses.mse import index_match_MSE
from levin_tm_module.testing import test

if __name__ == "__main__":
    
    # Set up data for ones test
    # inputs = []
    # labels = generate_ones(100)
    # Set up data for equal input_output test
    # inputs = [random.randint(0, 100) for _ in range(10)]
    # labels = copy.copy(inputs)
    # Set up index test
    inputs = []
    labels = list(range(100))

    # Set up context manager
    # stopping_cond = lambda a,b: True if a < 3 else False
    stopping_cond = 100000
    cm = ContextManager(inputs, labels, fitness_fn=index_match_MSE, stopping_cond=stopping_cond, max_steps=1000)

    # Main loop
    best_turing_machines = cm.run()
    if best_turing_machines == None:
        print("NO SOLUTIONS FOUND")
        exit()

    print("Number of TM's generated and tested: ", stopping_cond, "\n")
    print("Number of TM's with perfect prediction: ", len(best_turing_machines))

    test(best_turing_machines, inputs, labels)
    