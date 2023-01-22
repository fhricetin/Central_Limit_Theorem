# Central Limit Theorem


The values should be drawn independently of each other. -Values must come from the same distribution (although this requirement can be relaxed). The values ​​should come from a distribution with finite mean and variance. The number of values required to see convergence depends on the skewness of the distribution. The central limit theorem explains, at least in part, the prevalence of normal distributions in nature. Most traits of animals and other living organisms are influenced by various genetic and environmental factors, the effects of which are additive. Since the features we measure are the sum of many small effects, their distribution tends to be normalized. Another example is the weight of a bag of potato chips. This is actually the sum of the weights of many small independent contributions from each chip.

In this task, we simulate and observe the effect of the number of total values and the consequences of ignoring independent and identical sampling conditions. For this purpose, five different experimental setups should be implemented as follows:

Attempt 1: Two values are sampled and summed independently of the uniform standard distribution.

Attempt 2: Four values are sampled and summed independently of the uniform standard distribution.

Attempt 3: 50 values are sampled and summed independently of the uniform standard distribution

Attempt 4: 50 values are sampled and summed according to the uniform distribution. Dependencies are introduced by the following rules: If the value is less than 99, the next value is sampled from a uniform distribution between 0 and 200, otherwise between 99 and 101. 

Attempt 5: 50 values are sampled and summed independently of the various uniform distributions. Each time you generate a value, the uniform parameters (a and b-a) should be sampled from a standard uniform distribution.

For each experiment, we generate 200000 totals and create a pyplot figure containing their normalized histograms and the theoretical normal distribution curve. Implement and use your own normal probability density function. Experiments 1, 2 and 3 compute the theoretical mean and variance of the sum distribution and implement them explicitly. Experiments 4 and 5 estimate the mean and variance of the total distribution by performing calculations using the created sample set. To sample from a uniform distribution you can use the numpy.random.uniform() function.
