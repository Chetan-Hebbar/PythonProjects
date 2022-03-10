import random
import sys
import os
#Initialize wins and losses
wins=0
ties=0
losses=0
print('ROCK, PAPER, SCISSORS \n0 Wins, 0 Losses, 0 Ties')
while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    guess = str(input())

    if guess not in('ROCK','PAPER','SCISSORS','q'):
        print('Please enter one of the following: r,p,s,q!')
        continue
    robot_guess_int=random.randint(1,3)
    if robot_guess_int==1:
        robot_guess='ROCK'
    if robot_guess_int==2:
        robot_guess='PAPER'
    if robot_guess_int==3:
        robot_guess='SCISSORS'

    #DEBUG
    print('Robot Guess: ',robot_guess)

    if guess =='q':
        print('Thanks for playing!')
        sys.exit()

    if guess==robot_guess:
        ties=ties+1
        print('It is a tie!')
        print(str(wins)+' Wins, '+str(losses)+' Losses, '+str(ties)+' Ties')
        continue

    if (guess=='ROCK' and robot_guess=='PAPER') or (guess=='PAPER' and robot_guess=='SCISSORS') or (guess=='SCISSORS' and robot_guess=='ROCK'):
        losses=losses+1
        print('You Lose!')
        print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')

    else:
        wins=wins+1
        print('You Win!')
        print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')

print('Thanks for playing!')
