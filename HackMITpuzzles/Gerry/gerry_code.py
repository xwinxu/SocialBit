import json
import math
# from scipy.stats import norm

def norm_cdf(a, b):
    n = a + b
    p = (0.6*a + 0.4*b) / n
    q = 1 - p
    mu = n * p
    variance = n * p * q
    sigma = math.sqrt(variance)
    x = n / 2
    z = (x-mu) / sigma
    # P = 1 - norm.cdf(z)

    '''
    eff_gap = 0

    # If party A wins
    if P == 1:
        wasted_a = mu - (n-mu)
        wasted_b = b
    elif P == 0:
        wasted_a = a
        wasted_b = (n-mu) - mu

    eff_gap = (a-b) / n
    '''

    return [mu - n/2, sigma, n]

with open('gerry.json', 'r') as f:
    data = json.load(f)

a, b = data['voters_by_block']['party_A'], data['voters_by_block']['party_B']
a, b = [a[i:i+10] for i in range(0, len(a), 10)], [b[i:i+10] for i in range(0, len(b), 10)]
a, b = [list(i) for i in zip(*a)], [list(i) for i in zip(*b)]

total = 0
for i in range(10):
    for j in range(10):
        total += a[i][j] + b[i][j]

print(total/20)

# with open('output.csv', 'w') as f:
#     for i in range(10):
#         for j in range(10):
#             data = norm_cdf(a[i][j], b[i][j])
#             f.write('{:.1f} {:.1f} {},'.format(data[0], data[1], data[2]))
#         f.write('\n')

# District Population Imbalance:
# we assume the case where each district is the same. the 20 represents a summation, or sigma, and we
# use sigma because the districts are usually different. But in our case, we assume them to be the same
# 20 * (pop_district - pop_mean)^2 = 304*10^10
# pop_mean = pop_tot / 20
# solve for pop_district
# pop_district - pop_mean tells you how far you can vary population of districts
