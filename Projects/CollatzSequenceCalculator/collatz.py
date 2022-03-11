import sys

def collatz(number):
    if number % 2==0:
        return number // 2
    if number % 2==1:
        return (3*number) + 1

while True:
    try:
        num=int(input('Enter number:\n'))
    except ValueError:
        print('Error: Invalid Argument. Please enter an integer only.')
        continue

    iterations=0
    while num !=1:
        num = collatz(num)
        iterations=iterations+1
        print(num)

    print('Iterations to reach 1: ',iterations)
    sys.exit()