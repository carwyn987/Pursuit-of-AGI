
import random

from levin_tm_module.tm import TM
from levin_tm_module.executor import Executor

from levin_tm_module.program_generators.generator import generate_random_program

class ContextManager:
    """
    Context Manager (CM) defines an init program, program update algorithm (random, GA), success conditions
    CM should then repeatedly call executor for the program, compute fitness (with test data), and decide to continue or stop
    Arguments:
    ----------
     - Inputs (entire dataset)
     - Labels (entire dataset)
     - Initial Program
     - Program Update Algorithm
     - Fitness Function
     - Stopping Condition (# programs tested or appropriate fitness)
     - max_steps (int): Number of steps to run a program for before stopping.

    Returns:
    --------
     - best program
     - fitness
     - status
    """
    def __init__(self, inputs, labels, fitness_fn, stopping_cond, max_steps):

        self.inputs = inputs
        self.labels = labels
        self.fitness_fn = fitness_fn
        self.stopping_cond = stopping_cond
        self.max_steps = max_steps

        # Split data into train and test
        label_indxs = list(range(0,len(labels)))
        matching_format = list(zip(label_indxs,labels))

        # Sample labels
        self.train_input = []
        self.train_matching_format = random.sample(matching_format, 3)

        print("Training Data: ", self.train_matching_format)


    def run(self):
        
        # In a loop, set up a TM, set up an executor, run the executor, and track final fitnesses
        # best_fitness = 1e10
        count = 0
        while True:
            count += 1

            # Generate a random program
            program = generate_random_program()

            # Set up turing machine
            tm = TM()
            tm.setup_program(program)

            # Set up executor
            executor = Executor(tm, max_steps=self.max_steps, labels=self.train_matching_format, fitness_fn=self.fitness_fn)

            fitness, response, steps = executor.run()

            if self.stopping_cond(fitness, response):
                return count, tm, fitness, response, steps
