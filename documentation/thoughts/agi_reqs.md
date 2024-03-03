# Overview

This file contains my thoughts about necessary components for AGI.



## Strong Beliefs

 - Sample efficiency is necessary
 - The model should not learn to simply model the input data. It needs to learn to "learn", i.e. it needs to learn how to process new information into the network: how to add components, nodes, and structures, how to structure new information, where to connect, etc.
 - Simplistic modeling is better for (1) generalization purposes, and (2) compression. Occam's Razor + kolmogorov complexity are good ideas to work from in that respect.

## Weak Beliefs

 - The solution needs 3 main things: (1) data compression, (2) rule generation, and (3) experience recall. The rule generation + saving inputs let us "remember" or more likely compute the outcome.
 - An interesting experiment would be to pair a limited network size with a hierarchical builder, and using an evolutionary or gradient-based algorithm to optimize for a task. The small network would be optimized indirectly, using an end-to-end training methodology. The "builder" would be responsible for connecting many smaller identical networks (either identical architecture, or weights too?). In essance, this is a more flexible rnn/cnn architecture.

## Questions

 - Do memory and processing need to have a meaningful separation?
 - Humans seem to have a very basic understanding of correlations / equations of interdependence (trends). We seem to have good intuition about first and second order equations. In other words, we can understand correlation, and it's derivative. Such can be seen with our ability to determine and understand causal factors. It can become quite challenging to accurately extend our extrapolation beyond "increasing x results in an increasing y" or "increasing x results in a superlinear increase in y"
