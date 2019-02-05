import re
from BasePair import *

def basePairReader(filename, nucleoList):

    basePairList = []
    with open(filename, 'r') as f:
        for lines in f:
            lines = lines.split("\n")
            oneLine = lines[0].split(" ")

            firstIndex = oneLine[0]
            secondIndex = oneLine[1]

            firstInPair = None
            secondInPair = None
            for i in nucleoList:
                if i.index == firstIndex:
                    firstInPair = i
                if i.index == secondIndex:
                    secondInPair = i

                if (firstInPair is not None) and (secondInPair is not None):
                    break

            basePair = BasePair(firstInPair, secondInPair, oneLine[5], oneLine[4])
            basePairList.append(basePair)

    return basePairList