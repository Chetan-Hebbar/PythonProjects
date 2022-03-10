import random
import sys
import os

print('ROCK, PAPER, SCISSORS \n0 Wins, 0 Losses, 0 Ties \nEnter your move: (r)ock (p)aper (s)cissors or (q)uit')

guess = str(input())

if guess not in('r','p','s','q'):
    print('NOPE!')

print ('Input: '+guess)