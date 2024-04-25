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





## Scenario --> Conclusion (Also some EvoPsych BS)

 - We seem to know things in a (rule, exception) tuple. I know intuitively that when an object is let go of, it drops to the nearest structural platform. However, I also know that balloons rise when dropped. Realistically, children learn this quite fast. If a child is first introduced to a balloon at 5 years old, years after first recognizing that objects go "down", I speculate that it wouldn't break their entire world view, and that they would learn to associate balloons with rising quite fast. Probably wouldn't even question the other relation they have in their mind.

 - We learn discrete things, and we learn the sign of correlation quite well. Past that, our learning ability seems domain specific. Children learn that when they cry, they get tended to. But they don't easily pick up on *how* much they get tended to. Same with social situations: when I tell a joke, people laugh. But if you're one of the chosen ones who can decipher the equation of how much, you become an abnormally talented comedian.
 
 - 



## Issues in Intelligence - "Open Problems in Universal Induction & Intelligence" (Marcus Hutter)
 - **The GRUE problem**: We want to use Occams Razor to choose the simplest hypotheses as most likely. However, even in the formalization of AIXI, with kolmogorov complexity and solomonoff induction, this is dependent upon the primatives / instruction set we choose. In this manner, we can choose a primative such as "all emeralds are green until 2020 and blue after" to be simpler than "all emeralds are green".
 - **Black raven problem**: Take two attributes of objects, such as "animal" (raven = R) and "color" (black = B). To confirm (support) the hypothesis that all ravens are black (R-->B), we look to see many instances of R ^ B. But, seeing these objects also confirms that all black things are ravens (B-->R). Logically equivalent are (!B --> !R), by: "if all ravens are black, and we see an object that is not black, it is not a raven", and (!R --> !B): "if we see an object that is not a raven, it is not black". Unfortunately, this is also confirmed by seeing "white socks". So, seeing "white socks" confirms the hypothesis that "all ravens are black".
 - **Zero prior problem**: Assume a bayesian framework for "learning". When starting, we do not know a probability distribution of hypotheses. So, generally a continuous probability function is used for the prior belief in hypotheses. Any hypothesis that is not a range of hypotheses, such as statements of "all", "not", or "p=r in R" all have probabilities of zero. Therefore, the probability of these hypotheses is zero or undefined(?).
 - **Reparameterization Invariance**: In finite / discrete hypothesis classes, we can simply assign each hypothesis equal probabilities. However, in infinite hypothesis classes, this doesn't work. In "compact" classes (?), Jeffreys Prior works?
 - **Old Evidence/Updating Problem**: How to add old evidence to support a new hypothesis, or a new hypothesis to an existing model?
  - From arxiv (https://arxiv.org/abs/2402.04643): 
    """
    A very famous ``test'' of the General Theory of Relativity (GTR) is the advance of Mercury's perihelion (and of other planets too). To be more precise, this is not a prediction of General Relativity, since the anomaly was known in the XIXth century, but no consistent explanation had been found yet at the time GTR was elaborated. Einstein came up with a solution to the problem in 1914.
    In the case of Mercury, the closest planet to the Sun, the effect is more pronounced than for other planets, and observed from Earth; there is an advance of the perihelion of Mercury of about 5550~arc seconds per century (as/cy). Among these, about 5000 are due to the equinox precession (the precise value is {5025.645}~as/cy) and about 500 ({531.54}) to the influence of the external planets. The remaining, about 50~as/cy ({42.56}), are not understood within Newtonian mechanics. Here, we revisit the problem in some detail for a presentation at the undergraduate level. 
    """