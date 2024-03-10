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
    stopping_cond = lambda a,b: True if a < 3 else False
    cm = ContextManager(inputs, labels, fitness_fn=index_match_MSE, stopping_cond=stopping_cond, max_steps=1000)

    # Main loop
    num_turing_machines_tested, best_tm, fitness, status, steps = cm.run()
    print("Number of TM's generated and tested: ", num_turing_machines_tested)
    print("Final TM: ", best_tm.program_working_tape)
    print("Output Tape: ", best_tm.output_tape)
    print("Fitness: ", fitness)
    print("Exit: ", status)
    print(f"in {steps} steps")
    