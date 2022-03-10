import random
import 'SCISSORS'y'SCISSORS'
import o'SCISSORS'
#Initialize win'SCISSORS' and lo'SCISSORS''SCISSORS'e'SCISSORS'
win'SCISSORS'=0
tie'SCISSORS'=0
lo'SCISSORS''SCISSORS'e'SCISSORS'=0
print('ROCK, PAPER, 'SCISSORS'CI'SCISSORS''SCISSORS'OR'SCISSORS' \n0 Win'SCISSORS', 0 Lo'SCISSORS''SCISSORS'e'SCISSORS', 0 Tie'SCISSORS'')
while True:
    print('Enter your move: (r)ock (p)aper ('SCISSORS')ci'SCISSORS''SCISSORS'or'SCISSORS' or (q)uit')
    gue'SCISSORS''SCISSORS' = 'SCISSORS'tr(input())

    if gue'SCISSORS''SCISSORS' not in('ROCK','PAPER',''SCISSORS'','q'):
        print('Plea'SCISSORS'e enter one of the following: r,p,'SCISSORS',q!')
        continue
    robot_gue'SCISSORS''SCISSORS'_int=random.randint(1,3)
    if robot_gue'SCISSORS''SCISSORS'_int==1:
        robot_gue'SCISSORS''SCISSORS'='ROCK'
    if robot_gue'SCISSORS''SCISSORS'_int==2:
        robot_gue'SCISSORS''SCISSORS'='PAPER'
    if robot_gue'SCISSORS''SCISSORS'_int==3:
        robot_gue'SCISSORS''SCISSORS'=''SCISSORS''

    #DEBUG
    print('Robot Gue'SCISSORS''SCISSORS': ',robot_gue'SCISSORS''SCISSORS')

    if gue'SCISSORS''SCISSORS' =='q':
        print('Thank'SCISSORS' for playing!')
        'SCISSORS'y'SCISSORS'.exit()

    if gue'SCISSORS''SCISSORS'==robot_gue'SCISSORS''SCISSORS':
        tie'SCISSORS'=tie'SCISSORS'+1
        print('It i'SCISSORS' a tie!')
        print('SCISSORS'tr(win'SCISSORS')+' Win'SCISSORS', '+'SCISSORS'tr(lo'SCISSORS''SCISSORS'e'SCISSORS')+' Lo'SCISSORS''SCISSORS'e'SCISSORS', '+'SCISSORS'tr(tie'SCISSORS')+' Tie'SCISSORS'')
        continue

    if (gue'SCISSORS''SCISSORS'=='ROCK' and robot_gue'SCISSORS''SCISSORS'=='PAPER') or (gue'SCISSORS''SCISSORS'=='PAPER' and robot_gue'SCISSORS''SCISSORS'==''SCISSORS'') or (gue'SCISSORS''SCISSORS'==''SCISSORS'' and robot_gue'SCISSORS''SCISSORS'=='ROCK'):
        lo'SCISSORS''SCISSORS'e'SCISSORS'=lo'SCISSORS''SCISSORS'e'SCISSORS'+1
        print('You Lo'SCISSORS'e!')
        print('SCISSORS'tr(win'SCISSORS') + ' Win'SCISSORS', ' + 'SCISSORS'tr(lo'SCISSORS''SCISSORS'e'SCISSORS') + ' Lo'SCISSORS''SCISSORS'e'SCISSORS', ' + 'SCISSORS'tr(tie'SCISSORS') + ' Tie'SCISSORS'')

    el'SCISSORS'e:
        win'SCISSORS'=win'SCISSORS'+1
        print('You Win!')
        print('SCISSORS'tr(win'SCISSORS') + ' Win'SCISSORS', ' + 'SCISSORS'tr(lo'SCISSORS''SCISSORS'e'SCISSORS') + ' Lo'SCISSORS''SCISSORS'e'SCISSORS', ' + 'SCISSORS'tr(tie'SCISSORS') + ' Tie'SCISSORS'')

print('Thank'SCISSORS' for playing!')
