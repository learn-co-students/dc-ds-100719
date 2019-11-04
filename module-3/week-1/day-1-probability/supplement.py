def prob_of_E(outcomes, num_of_heads):
    """
    :param outcomes: np.array - [experiment_size, n_trials]
    :param num_of_heads: int. Event is the getting num_of_heads or more.
    :return: float - returns the frequency of event getting num_of_heads or more given outcomes
    """
    n_E = (outcomes[:,0] >= num_of_heads).sum()
    return n_E/len(outcomes)

probabilities = []

for i in range(1, 10001):
    experiment = np.random.multinomial(n = 2, pvals =[0.5, 0.5], size = i)
    prob = prob_of_E(outcomes = experiment, num_of_heads=1)
    probabilities.append(prob)

%matplotlib inline

plt.plot(range(1, 10001, 100),
         probabilities[::100]);


## define a function that returns factorials
def factorial(n):
    product = 1

    while n != 0:
        product *= n
        n -= 1
    return product