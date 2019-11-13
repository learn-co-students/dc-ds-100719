#population mean
mu = 500

# let's find the sample mean
x_bar = sample.mean()

# know let's find the standard error
# note that we don't know the population standard deviation
# so instead we will use sample standard deviation as an estimator

s = sample.std(ddof = 1)/np.sqrt(len(sample))

# know we will find a t-score by dividing the difference in means
# with standard error

t = (x_bar - mu)/s

# note that we know that t-score should lie on a t-distribution with
# degrees of freedom len(sample) - 1 as the parameter.
# let's use t method from scipy.stats

p_value = stats.t.sf(t, df = len(sample) -1)


## two sample t-test assuming same population variance
n1 = len(sample1)
n2 = len(sample2)

pooled_std = np.sqrt(((n1-1)*np.var(sample1, ddof =1) + (n2-1)*np.var(sample2, ddof = 1))/(n1+n2-2))

denom = pooled_std*np.sqrt(1/n1 + 1/n2)

num = sample1.mean() - sample2.mean()

t = num/denom

## use of two sample t-test directly from scipy.stats
stats.ttest_ind(sample1, sample2, equal_var=True)