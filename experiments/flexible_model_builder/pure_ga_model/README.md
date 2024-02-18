# Overview
Fit an equation to data using a Genetic Algorithm (GA)


## Details
Need a way to represent a chromosome
 - Perhaps ascii: (a+b^2), and verify correctness with bracket matching and other necessary rules (^ followed by var or value)
 - Likely existing libraries for this.

Mutations and crossovers are random, but require correctness checking

Loss function compensates for loss and length of chromosome using Solomonoff rules / Kolmogorov complexity.

## Scope of Intent
i.e. "What question do I want answered? What will foreseeably be added to this question?"

 - Given a (potentially noisy) dataset containing measured values within kinematic equations, such as (v0, vf, a, t) for "vf = v0 + at" or (d, v0, a, t) for "d = v0t + at^2", find the minimal equation that represents this data.
 - Is it possible to characterize subgraphs as useful for solving problems, and then using this as an abbreviated (memory efficient) graph substructure?

## Necessary Qualities
 - Flexible operations - supports addition, subtraction, multiplication, exponentiation, and even operations that are not differentiable such as ORs, bit shifts, etc.
 - Flexible structure - supports adding nodes anywhere where correctness is maintained, so long as the graph is a DAG.
 - Some way to encourage crossover
 - Some way to encourage shorter length chromosomes, while allowing for growth.

## Extensions
Possible Extensions:
 - Support acyclic "memory structure"
 - Supports time-synchronous propagation as well as / as an alternative to threshold-based propagation (spiking NN's)
 - Include rules for gradient variables passed in as input (i.e. specify pos, vel, accel). May provide ability to benefit from autograd
 - Include some sort of analysis on noise type (?) such that we can fit an assumed noise distribution (providing insight when to generalize).

## Sources
 - https://en.wikipedia.org/wiki/Eureqa 
 - 