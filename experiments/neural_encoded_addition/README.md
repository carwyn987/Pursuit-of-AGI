# Theory

Neural networks are known to be universal function approximators. Therefore, neural networks should be able to  approximate addition, subtraction, exponentiation, and any other imaginable function. However, it is known that to approximate the functions to k digits of precision, at least one hidden layer with an arbitrarily large number of nodes (parameterized on k) is necessary. 

However, I theorize (with high confidence) that the minimal neural network required to capture the addition operator is a network with two inputs, one output, no activation functions, and no biases necessary, as shown below.

### Network Structure:

Inputs: x, y
Output node: o


  (x)   (y)
 w1 \   / w2
     (0)

### Optimal Solution
Function to approximate: f(x,y) = x+y
Optimal output = x + y
True neural network function: f(x,y) = w1 * x + w2 * y
Optimal weights are therefore
w1 | w2
-------
1  | 1 
The learned function becomes f(x,y) = 1*x + 1 * y = x + y

Note: If a bias is present, the optimal value is 0, as the true neural network function becomes f(x,y) = w1 * x + w2 * y + b.