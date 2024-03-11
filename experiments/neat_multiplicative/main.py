"""
2-input product example -- this is most likely the simplest possible example.
"""

import os
import sys
import neat
import visualize

sys.path.insert(0, os.path.join("/", *os.path.realpath(__file__).split("/")[:-2], "neural_encoded_multiplication/"))
from multiplication_data_generator import multiplication_data_generator

# 2-input XOR inputs and expected outputs.
# xor_inputs = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
# xor_outputs = [(0.0,), (1.0,), (1.0,), (0.0,)]

# Generate product data
xor_inputs = []
xor_outputs =[]

i1, i2, o1 = zip(*multiplication_data_generator(N=10))
xor_inputs = list(zip(i1,i2))
xor_outputs = [(x,) for x in o1]

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 4.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(xor_inputs, xor_outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0] - xo[0]) ** 2


def run(config_file):
    save_path = 'experiments/neat_multiplicative/data/'

    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(5, filename_prefix=save_path + 'neat-checkpoint-')) # generates tons of files so no thanks

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 20)
    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    for xi, xo in zip(xor_inputs, xor_outputs):
        output = winner_net.activate(xi)
        print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))
        
    node_names = {-1: 'Input 1', -2: 'Input 2', 0: 'Output'}
    visualize.draw_net(config, winner, True, node_names=node_names, filename=save_path+'1')
    # visualize.draw_net(config, winner, True, node_names=node_names, prune_unused=True, filename=save_path+'2')
    # visualize.plot_stats(stats, ylog=False, view=True, filename=save_path+'avg_fitness.svg')
    # visualize.plot_species(stats, view=True, filename=save_path+'speciation.svg')

    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    # p.run(eval_genomes, 10)
        
    print("Winner: ", winner)

    # Print nodes
    print("Nodes:")
    for _, node in winner.nodes.items():
        print(f"Node : {node}")

    # Print connections
    print("\nConnections:")
    for _, conn in winner.connections.items():
        print(f"Connection: {conn}")


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path)