#hort.py
# Program to flip a coin

import random

flip = random.randint(0, 1 )
if (flip == 0):
	flip = "Heads"
else :
	flip = "Tails"

print("I flipped a coin and i got: " + flip + "!!!")


