# Bayesian Analysis

### Team
- Animesh Madaan
- Arush Upadhyaya
- Sankalp Mittal
- Maharaajan J
- Wattamwar Akanksha Balaji

### Instructions
This is a source code written in `python`. This can be run on any machine having a python interpreter installed. 

Ensure that the aforementioned interpreter is added to `PATH`

- Go to the directory in which the code is saved 
- Install the requirements
```bash 
pip install -r requirements.txt
```
- Run the following command in the *terminal* 
```bash
python main.py
```
# Logic

## 1. Key Concepts

- **Prior Distribution**: The prior distribution represents our initial beliefs about the parameters of interest before observing any data. It encodes our prior knowledge or assumptions about the problem at hand.

- **Posterior Distribution**: The posterior distribution is the updated distribution of the parameters after taking into account the observed data. It combines the prior distribution with the likelihood of the data to provide a revised estimate of the parameter values.

- **Maximum Likelihood Estimation (MLE)**: MLE is a method for estimating the parameters of a probability distribution by maximizing the likelihood function. In the context of a coin toss experiment, MLE estimates the bias of the coin that is most likely to have generated the observed data.

- **Maximum A Posteriori (MAP) Estimation**: MAP estimation is similar to MLE but incorporates the prior distribution. It estimates the parameters by maximizing the posterior distribution, which is proportional to the product of the likelihood and the prior. MAP estimation takes into account both the observed data and the prior beliefs.

## 2. Comparison of Prior Distributions

The four prior distributions considered in this experiment are:

1. **Beta(2, 5)**: This prior assumes that the coin is more likely to be biased towards tails. It suggests a prior belief that the probability of obtaining heads is lower than the probability of obtaining tails.

2. **Beta(5, 2)**: Conversely, this prior assumes that the coin is more likely to be biased towards heads. It indicates a prior belief that the probability of obtaining heads is higher than the probability of obtaining tails.

3. **Beta(1, 1)**: Also known as the uniform prior, this distribution assumes no prior knowledge or bias about the coin's probability of landing on heads or tails. It gives equal weight to all possible values of the bias parameter.

4. **Beta(2, 2)**: This prior assumes a slight preference towards a fair coin. It suggests a prior belief that the coin is more likely to have a balanced probability of landing on heads or tails.

The choice of prior distribution influences the posterior distribution. A prior that aligns well with the true bias of the coin will lead to a posterior distribution that is more concentrated around the true value. On the other hand, a prior that is far from the true bias may result in a posterior distribution that is less informative or requires more data to converge to the true value.

## 3. MLE and MAP Estimates

The MLE and MAP estimates for each prior distribution are summarized in the following table:

| Prior Distribution | MLE Estimate | MAP Estimate |
|-------------------|----------------|-----------------|
| Beta(2, 5)        |  0.60          |  0.47           |
| Beta(5, 2)        |  0.60          |  0.67           |
| Beta(1, 1)        |  0.60          |  0.60           |
| Beta(2, 2)        |  0.60          |  0.58           |

The MLE estimate remains the same across all priors since it only considers the observed data. However, the MAP estimate varies depending on the prior distribution used. The MAP estimate takes into account both the observed data and the prior beliefs, providing a balance between the two sources of information.