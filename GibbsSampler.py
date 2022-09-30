# Given: Integers k, t, and N, followed by a collection of strings Dna.

# Return: The strings BestMotifs resulting from running GibbsSampler(Dna, k, t, N) with 20 random starts

import random

file = open('inputGibbs', 'r')
k, t, n = [int(i) for i in file.readline().strip().split(' ')]
dna = [i.strip() for i in file.readlines()]


def randomMotifs(dna, k):    # runs n times
    motifs = []
    # generate random k-mers
    for seq in dna:
        index = random.randint(0, len(seq) - k)
        motifs.append(seq[index:index + k])
    return motifs


def profileMatrix(motifs, k): # runs n^2 times
    profile = []
    # iterate through motifs and add 1 to letter count if found at index
    for i in range(k):
        for j in range(len(motifs)):
            # base case for formatting
            if j == 0:
                profile.append({'A': 1, 'T': 1, 'C': 1, 'G': 1})
            profile[i][motifs[j][i]] += 1
    return profile


def score(motifs, k, t):  # runs in O(n^2) by profileMatrix call
    profile = profileMatrix(motifs, k)
    score = 0
    for i in range(len(profile)):
        score = score + (4 + t - profile[i][max(profile[i], key=profile[i].get)])
    return score


def GibbsSampler(dna, k, t, n):  # O(n^3) since profileMatrix has runtime n^2 and would need to be called inside the for loop
    # randomly select kmers
    motifs = randomMotifs(dna, k)
    bestMotifs = list(motifs)
    for j in range(n):
        # i = random(t)
        i = random.randint(0, t - 1)
        # all strings except motifs[i]
        motifs.pop(i)
        # generate random kmers from ith sequence
        # failed to implement the randomly generated k-mer in ith sequence
        # update best motifs if better score found
        if score(motifs, k, t) < score(bestMotifs, k, t):
            bestMotifs = list(motifs)
    return bestMotifs

# base comparison
bestMotifs = GibbsSampler(dna, k, t, n)
# run 20 times and take best scoring motif
