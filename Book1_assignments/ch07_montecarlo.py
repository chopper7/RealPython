# Monte Carlo simulation example, Real Python Part 1, p. 90

from random import randint

# Accumulators to track how many heads, how many tails
heads = 0
tails = 0

# Running many times (large sample size) to simulate long-term outcome
for trial in range(0, 10000):
    # Assuming 0 is tails, 1 is heads, "toss coin" as long as result is "tails"
    while randint(0, 1) == 0:
        tails += 1
    heads += 1

# Proportion of heads to tails
proportion = heads / tails

print("heads / tails = ", proportion)
