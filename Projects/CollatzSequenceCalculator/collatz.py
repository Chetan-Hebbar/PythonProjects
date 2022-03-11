import sys

#This is the collatz operator. Divide by 2 for even numbers, and 3x+1 for odd numbers.
def collatz(number):
    if number % 2==0:
        return number // 2
    if number % 2==1:
        return (3*number) + 1

# Kept the main driver in a while loop, to allow for retries when the input exception is caught
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