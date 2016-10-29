# Real Python part 1, ch 07, p. 92.

'''
Write a script "election.py" that will simulate an election between two
candidates, A and B.
One of the candidates will win the overall election by winning a majority of
the regional elections. (Here, a candidate wins the overall election by
winning at least two regional elections.)
Candidate A has the following odds:
87% chance of winning region 1
65% chance of winning region 2
17% chance of winning region 3

Import and use the `random()` function from the `random` module to simulate
events based on probabilities; this function doesn't take any arguments(you
don't pass it any input) and returns a random value somewhere between 0 and 1.
(e.g., 0.6702591868).

Simulate 10,000 such elections, then (based on the average results) display the
probability that Candidate A will win and the probability that Candidate B will
win.
Hint: You'll probably need to use a for-loop with a lot of if-else statements
to check the results of each regional election.
'''

# Simulate the results of an election using a Monte Carlo simulation

from random import random

total_A_election_wins = 0
total_B_election_wins = 0

# Run an election simulation this many times, in order to produce broad trends:
election_trials = 100000

for trial in range(0, election_trials):
    A_win = 0
    B_win = 0
    # Call `random()` once for each region, comparing its randomly-returned
    # value to candidate A's probability of winning that region.
    # 1st region
    if random() < .87:
        A_win += 1
    else:
        B_win += 1
    # 2nd region
    if random() < .65:
        A_win += 1
    else:
        B_win += 1
    # 3rd region
    if random() < .17:
        A_win += 1
    else:
        B_win += 1
    # calculate the trial's election outcome
    if A_win > B_win:
        total_A_election_wins += 1
    else:
        total_B_election_wins += 1


print("Probability A wins:", total_A_election_wins / election_trials)
print("Probability B wins:", total_B_election_wins / election_trials)
