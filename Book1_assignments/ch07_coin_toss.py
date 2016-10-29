# Real Python part 1, ch 07, p. 93.
'''
Simulate a coin toss experiment
Write a script "coin_toss.py" that uses coin toss simulations to determine the
answer to this slightly more complex probability puzzle:
I keep flipping a fair coin until I've seen it land on both heads and tails at
least once each - in other words, after I flip the coin the first time, I
continue to flip it until I get a different result.
On average, how many times will I have to flip the coin total? Again, the actual
probability could be worked out, but the point here is to simulate the event
using `randint()`. To get the expected average number of tosses, you should set
a variable trials = 10000 and a variable flips = 0, then add 1 to your flips
variable every time a coin toss is made. Then you can print flips / trials at
the end of the code to see what the average number of flips was.
'''


from random import randint

flips = 0
trials = 10000

for trial in range(0, trials):
    heads, tails = False, False
    while not (heads and tails):
        flip = randint(0, 1)
        if flip == 0:
            heads = True
            flips += 1   # added this line after viewing answer code
        else:
            tails = True
            flips += 1   # added this line after viewing answer code
        #flips += flip   # commented out this line after viewing answer code

# How many flips per trial does it take to get at least one head and one tail?
print(flips / trials)
