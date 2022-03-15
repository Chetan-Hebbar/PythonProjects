import random

numberOfStreaks = 0
print('Enter number of flips per iteration')
numFlips=int(input())

print ('Enter length of streak to test')
numStreak=int(input())

def StreakChecker(genlist, streaklength, i):
    refvalue = genlist[i]
    for n in range(1, streaklength):
        if genlist[i + n] != refvalue:
            return False
    return True


def CreateHeadsTailsList(length):
    SampleList = []
    for i in range(length):
        val = random.randint(0, 1)
        if val == 0:
            list.append(SampleList, 'H')
        else:
            list.append(SampleList, 'T')
    return (SampleList)


def CheckForStreaks(genlist, StreakLength):
    for i in range(0, len(genlist) - StreakLength + 1):
        # Check List[i] through List[i+StreakLength-1]
        isStreak = StreakChecker(genlist, StreakLength, i)
        # print(str(i)+ ', '+ List[i+Length-1])
        if isStreak == True:
            return isStreak
    return False


GeneratedList = (CreateHeadsTailsList(numFlips))
print(CheckForStreaks(GeneratedList, numStreak))
