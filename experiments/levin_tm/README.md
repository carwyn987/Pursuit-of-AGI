# Overview

An implementation of the Turing-Machine based machine learning algorithm described within "Discovering Problem Solutions with Low Kolmogorov Complexity and High Generalization Capability" by Jürgen Schmidhuber (1994). Within this sub-directory, I have matched some of the results of the paper, and verified the impressive generalization ability.

# Design

![UML-ish Design](media/TM-Levin.png)

# Notes

The turing machine program-tape method formalized here as the foundation on which to apply learning algorithms has  impressive generalization ability. The intuitive explanation for this is that by describing data by its generation rules, significant compression in storage size can be achieved - as implied by Kolmogorov complexity.

There are shortcomings to this approach, however. First, the Grue problem described by Marcus Hutter in "Open Problems in Universal Induction & Intelligence" (2009), and originally denoted by Nelson Goodman's "Fact, Fiction, and Forecast" is present. Simply put, the instruction set / predicates available to programs implicitly impact the complexity of programs. Due to the arbitrary nature or instructions, one could define a new instruction as any long and complex program to make it equivalent to the simplest of programs. Second, as mentioned in the paper, increasing the size of the instruction set or working tape leads to the "code explosion" issue, where as code choices expand, "there is more material with which to form new programs" (Schmidhuber, Page 17). The final shortcoming I will list here, noting that in no way is this a comprehensive list, is that the currently implemented instruction set is quite suboptimal for realistic data. Apart from the gaping issue involved with failure to deal with noisy data, generating common physics-involved floating point values (such as gravity = 9.81..., pi = 3.14...) requires derivation, rather than fitting. Given a dataset containing distance, and time of objects dropped from various altitudes above earths surface, an incremental algorithm is required for convergence to occur within a realistic timeframe (which is discussed in section 5).