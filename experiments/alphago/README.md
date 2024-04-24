# Overview

Emulating AlphaGo's deep reinforcement learning algorithm.
 - Policy eval + improvement
 - Monte Carlo Tree Search (MCTS) + rollout

# Plan

Network:
 - Input:
  - 19x19x8
   - 19x19 is the size of the game board. 2 of those each as a binary mask for black and white pieces. 4 of those for the previous 4 "states"
   - Likely <19 to make it locally trainable.
 - Output:
  - With the output, I want to be able to determine the value of the current state, and P(a|s). So either I have an output grid, representing the values of taking further actions, or I assume the action as part of the input. Or I can have the NN learn V(s) and then run it once for every move to determine the most probable move?