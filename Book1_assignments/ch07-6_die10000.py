# Simulate 10,000 rolls of a die (dice)

from random import randint

# Counters
total = 0  # running sum of dice results
throws = 10000

for trial in range(0, throws):
    total += randint(1, 6)

# Average die roll result
dice_avg = total / throws

print("Average of 10,000 rolls of the 'die' = ", dice_avg)
