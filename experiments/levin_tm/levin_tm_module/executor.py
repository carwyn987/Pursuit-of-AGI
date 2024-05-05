from levin_tm_module.losses.mse import MSE

class Executor:
    def __init__(self, tm, max_steps, labels, fitness_fn=MSE):
        """
        The executor is responsible for executing a single program until halting or stopping conditions are met.

        Arguments:
        ----------
         - tm (TuringMachine): A turing machine assumed to be in the initialized state (empty working tape, loaded program tape, loaded input tape)
         - max_steps (int): Maximum number of instructions to run
         - labels (list): Expected output tape
         - fitness_fn (function): function that computes returned fitness
        """

        self.fitness_fn = fitness_fn
        self.tm = tm
        self.max_steps = max_steps
        self.labels = labels

    def run(self):
        """
        Run tm until final state

        Returns:
        ----------
         - fitness (float): Computed fitness between output tape and expected output, according to passed in or default fitness function
         - final_status (int): 0 = running, 1 = halted, -1 = failure to apply
        """

        iters = 0
        response = self.tm.apply()
        # While running and less than max_steps
        while response != -1 and response != 1 and iters < self.max_steps:
            iters += 1
            response = self.tm.apply()

        # Now that run is complete, parse response
        fitness = self.fitness_fn(self.tm.output_tape, self.labels)
        # print(iters, fitness, response, self.tm.program_working_tape)
            
        return fitness, response, iters