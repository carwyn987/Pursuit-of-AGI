# Directory Purpose
Here, I wish to explore the ability of NEAT to learn a simple multiplication function. This will serve to understand the typical process of NEAT's learning, as well as verify that NEAT has the ability to swap out aggregation functions (using the multiplicative function will allow for the network to converge with two input nodes, one output node, no hidden nodes, and no activation).

This is built off of the XOR example in the NEAT repository.

# NEAT Overview

NeuroEvolution of Augmented Topologies (NEAT) is a method of appling a genetic algorithm to learn an optimal neural network - "an integrated scheme combining connectivity and weights" (Radcliffe 1993), the "Holy Grail in this area" (Radcliffe 1993).

NEAT has three main factors contributing to it's success:
 - Tracking historical origin to (1) provide a metric for the homology of networks, and (2) address the competing conventions problem, and ensure that crossover produces non-damaged offspring.
 - Protecting topological innovation (network structure diversity) with speciation (also known as niching). Explicit fitness sharing is applied within a species such that "the number of networks that can exist in the population on a single fitness peak is limited by the size of the peak".
  - Incremental growth from a minimal-dimension topology. This ensures the search space is minimized, and provides a significant advantage over fixed-topology NE systems.


# Paper Reflection and Evaluation
 - I quite enjoyed reading this paper. Using innovation numbers for verifiction of crossover compatibility and the combination of speciation and explicit fitness sharing to ensure topological diversity is very clever.
 - The implicity concept of “growth only” feels insufficient for “learning” complex generalizations. In a human capacity, synaptic pruning within the brain indicates that we do not follow this principle.
 - I failed to understand the exact structure of the networks generated from the paper. From the NEAT documentation, it seems like multiple activation functions can be defined and learned through mutation, as well as the aggregation functions (includes summation, product, max, min, maxabs, median, mean).
 - NEAT supports recurrent connections!
 - NEAT grows the network incrementally through mutation from a minimal topology. Therefore, penalizing the size of the network, as occams razor implies (especially when in the context of solomonoff induction) is unecessary.


# Further Research Areas
 - Non-markovian tasks
 - Enforced Subpopulations (ESP) (Gomez and Miikkulainen, 1999)
 - Cellular Encoding (Gruau, 1993)
 - Indirect vs direct  encoding schemes for networks
 - Structured Genetic Algorithm (sGA) ((Dasgupta and McGregor, 1992)
 - Parallel Distributed Genetic Programming (PDGP) System
 - GeNeralized Acquisition of Recurrent Links (GARL)
 - Dual Representation Scheme (for NNs) (Pujol and Poli, 1997)
 - Evolutionary Learning (Yao and Liu, 1996)
 - Competing Conventions Problem (Montana and Davis, 1989), Permutations Problem (Radcliffe, 1993)
 - Non Redundant Genetic Encoding (Thierens, 1996)
 - Gene Amplification (Darnell and Doolittle, 1986)
 - Speciationn / Niching with GA’s
 - Speciation applied to multimodal function optimization (Mahfoud, 1995)
