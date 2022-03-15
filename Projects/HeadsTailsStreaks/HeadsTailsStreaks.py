import random

numberOfStreaks = 0


def CreateHeadsTailsList(length):
    SampleList = []
    for i in range(length):
        val = random.randint(0, 1)
        if val == 0:
            list.append(SampleList, 'H')
        else:
            list.append(SampleList, 'T')
    return (SampleList)

def CheckForStreaks(List,Length):
    for i in range(0,len(List)-Length+1):
        print(str(i)+ ', '+ List[i+Length-1])


List=(CreateHeadsTailsList(100))
print(CheckForStreaks(List,10))