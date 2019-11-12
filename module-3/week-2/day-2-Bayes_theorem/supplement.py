def create_dist(sample, parameters=[5, 1]):
    mu = parameters[0]
    sigma = parameters[1]

    X = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)

    plt.plot(X, norm.pdf(X, loc=mu, scale=sigma))

    plt.scatter(sample, norm.pdf(sample, loc=mu, scale=sigma), color='r')

    plt.show()
    
with open('sample.pickle', 'rb') as handle:
    s = pickle.load(handle)