# Given: A string Genome, and integers k, L, and t.

# Return: All distinct k-mers forming (L, t)-clumps in Genome.

sequence = str(input("Genome:"))
k = int(input("k:"))
L = int(input("L:"))
t = int(input("t:"))


def frequencyTable(text, k):
    freqMap = {}
    n = len(text)
    for i in range(0, n - k + 1):
        pattern = text[i:i + k]
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] += 1
    return freqMap


def findClumps(text, L, k, t):
    patterns = {}
    n = len(text)
    for i in range(0, n-L+1):
        window = text[i:i + L]
        freqMap = frequencyTable(window, k)
        for s in freqMap:
            if freqMap[s] >= t:
                patterns[s] = freqMap[s]
    ans = patterns.keys()
    out = ','.join(ans)
    print(out)

findClumps(sequence, L, k, t)
