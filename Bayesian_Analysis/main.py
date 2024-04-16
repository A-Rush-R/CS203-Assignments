import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Observation
observation = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0] # 1 for H, 0 for T

# Count the number of heads and tails
heads_count = sum(observation) #since heads is 1
tails_count = len(observation) - heads_count

# Priors
priors = [(2, 5), (5, 2), (1, 1), (2, 2)]
closeness_list = []

# Create a figure and subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

# Plot the posterior and prior distributions
x = np.linspace(0, 1, 1000)

for i, (a, b) in enumerate(priors):
    posterior_a = a + heads_count
    posterior_b = b + tails_count
    
    # Calculate the prior and posterior distributions
    prior = beta.pdf(x, a, b)
    posterior = beta.pdf(x, posterior_a, posterior_b)
    
    # Plot the prior distribution
    axes[i].plot(x, prior, label=f'Prior: Beta({a}, {b})')
    
    # Plot the posterior distribution
    axes[i].plot(x, posterior, label=f'Posterior: Beta({posterior_a}, {posterior_b})')
    
    # Calculate MLE and MAP estimates
    mle = heads_count / len(observation)
    map_estimate = (posterior_a - 1) / (posterior_a + posterior_b - 2)
    closeness_list.append((abs(mle - map_estimate), (a, b), mle, map_estimate))
    
    # Plot MLE and MAP estimates
    axes[i].axvline(x=mle, color='black', linestyle='--', label=f'MLE ({mle:.2f})')
    axes[i].axvline(x=map_estimate, color='red', linestyle='--', label=f'MAP ({map_estimate:.2f})')
    
    axes[i].set_xlabel('Bias')
    axes[i].set_ylabel('Probability Density')
    axes[i].set_title(f'Prior and Posterior Distributions - Case: Beta({a}, {b})')
    axes[i].legend()

plt.tight_layout()
plt.show()

# Sort cases based on closeness to MLE and create a list of distribution parameters, MLE, and MAP
sorted_cases = sorted(closeness_list, key=lambda x: x[0])
sorted_params = [(params, mle, map_estimate) for _, params, mle, map_estimate in sorted_cases]

# Print the order of closeness to MLE with distribution parameters, MLE, and MAP
print("The order of closeness to MLE (Beta distribution parameters, MLE, MAP) in decreasing order:")
for params, mle, map_estimate in sorted_params:
    print(f"Beta{params}, MLE: {mle:.2f}, MAP: {map_estimate:.2f}")