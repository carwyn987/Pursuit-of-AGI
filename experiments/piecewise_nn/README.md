# Overview

Many processes are rather piecewise, expecially in how we come to realize them. For example, when a ball is dropped, we expect it to follow F = GMm/r^2, which we arrived at with approximation of experimental results. However, when a ball is dropped from high enough, we use separate equations to dictate its movements. Particularly, we include air resistance, which introduces some terminal velocity. However, if the ball is dropped even higher - in space, this effect is nullified, as there is no air resistance to slow the fall.

If I train a neural network on an accurate physics engine and relevant paremeters, it will approximate the underlying mechanical equations. However, this flies in the face of the way humans approach the problem - that is, modularly and hierarchically.

In this directory, I explore the idea of "piecewise" neural networks, that are able to approximate different effects individually. I will likely approach this with heavy regularization to promote simplicity.

One Idea: Have a bunch of individual small neural networks that train on a specific range, which they also output. That way, they learn not only to predict, but when that prediction is valid.

(I1)             (I2)           (I3)

(H1)             (H2)           (H3)

(O1)             (O2)           (O3)
 ^
Prediction    Start valid      End Valid

Issue: They will learn to predict a very small valid range (i.e. overfit)
 - Train with loss including a term for length of valid range?