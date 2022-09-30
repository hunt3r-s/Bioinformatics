# Given: A string BWT(Text), followed by a collection of strings Patterns.

# Return: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.

Sample Dataset
import sys


def lastToFirstMap(BWT, patterns):
    charCount = {}
    charIndexes = []
    for char in BWT:
        if char in charCount.keys():
            charCount[char] = charCount[char] + 1
        else:
            charCount[char] = 1
        i = char + str(charCount[char])
        charIndexes.append(i)

    firstCol = sorted(charIndexes, key=lambda x: x[0])

    lastToFirst = []
    for last in charIndexes:
        for i, first in enumerate(firstCol):
            if first == last:
                lastToFirst.append(i)

    return lastToFirst


def BWMatching(lastCol, pattern):

    lastToFirst = lastToFirstMap(BWT,pattern)
    top = 0
    bottom = len(lastCol) - 1

    result = []
    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            matches = []

            for i in range(top, bottom + 1):
                if lastCol[i] == symbol:
                    matches.append(i)

            if len(matches) != 0:
                top = lastToFirst[min(matches)]
                bottom = lastToFirst[max(matches)]
            else:
                return 0
        else:
            return bottom - top + 1

    

def getMatches(BWT,pattern):
  output = []
  for pattern in patterns:
    output.append(BWMatching(BWT, pattern))
  return output


f = open("input.txt", "r")
input = f.read().splitlines()
BWT = input[0]
patterns = input[1].split()
f.close()

matches = getMatches(BWT, patterns,)
print(*matches)
