# Given: Two amino acid strings.

# Return: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty σ = 5. (If multiple local alignments achieving the maximum score exist, you may return any one.)

Sample Dataset
PAM250 = {
    'A': {'A': 2, 'R': -2, 'N': 0, 'D': 0, 'C': -2, 'Q': 0, 'E': 0, 'G': 1, 'H': -1, 'I': -1, 'L': -2, 'K': -1, 'M': -1,
          'F': -3, 'P': 1, 'S': 1, 'T': 1, 'W': -6, 'Y': -3, 'V': 0, 'B': 2, 'Z': 1},
    'R': {'A': -2, 'R': 6, 'N': 0, 'D': -1, 'C': -4, 'Q': 1, 'E': -1, 'G': -3, 'H': 2, 'I': -2, 'L': -3, 'K': 3, 'M': 0,
          'F': -4, 'P': 0, 'S': 0, 'T': -1, 'W': 2, 'Y': -4, 'V': -2, 'B': 1, 'Z': 2},
    'N': {'A': 0, 'R': 0, 'N': 2, 'D': 2, 'C': -4, 'Q': 1, 'E': 1, 'G': 0, 'H': 2, 'I': -2, 'L': -3, 'K': 1, 'M': -2,
          'F': -3, 'P': 0, 'S': 1, 'T': 0, 'W': -4, 'Y': -2, 'V': -2, 'B': 4, 'Z': 3},
    'D': {'A': 0, 'R': -1, 'N': 2, 'D': 4, 'C': -5, 'Q': 2, 'E': 3, 'G': 1, 'H': 1, 'I': -2, 'L': -4, 'K': 0, 'M': -3,
          'F': -6, 'P': -1, 'S': 0, 'T': 0, 'W': -7, 'Y': -4, 'V': -2, 'B': 15, 'Z': 4},
    'C': {'A': -2, 'R': -4, 'N': -4, 'D': -5, 'C': 12, 'Q': -5, 'E': -5, 'G': -3, 'H': -3, 'I': -2, 'L': -6, 'K': -5,
          'M': -5, 'F': -4, 'P': -3, 'S': 0, 'T': -2, 'W': -8, 'Y': 0, 'V': -2, 'B': -3, 'Z': -4},
    'Q': {'A': 0, 'R': 1, 'N': 1, 'D': 2, 'C': -5, 'Q': 4, 'E': 2, 'G': -1, 'H': 3, 'I': -2, 'L': -2, 'K': 1, 'M': -1,
          'F': -5, 'P': 0, 'S': -1, 'T': -1, 'W': -5, 'Y': -4, 'V': -2, 'B': 3, 'Z': 5},
    'E': {'A': 0, 'R': -1, 'N': 1, 'D': 3, 'C': -5, 'Q': 2, 'E': 4, 'G': 0, 'H': 1, 'I': -2, 'L': -3, 'K': 0, 'M': -2,
          'F': -5, 'P': -1, 'S': 0, 'T': 0, 'W': -7, 'Y': -4, 'V': -2, 'B': 4, 'Z': 5},
    'G': {'A': 1, 'R': -3, 'N': 0, 'D': 1, 'C': -3, 'Q': -1, 'E': 0, 'G': 5, 'H': -2, 'I': -3, 'L': -4, 'K': -2,
          'M': -3, 'F': -5, 'P': 0, 'S': 1, 'T': 0, 'W': -7, 'Y': -5, 'V': -1, 'B': 2, 'Z': 1},
    'H': {'A': -1, 'R': 2, 'N': 2, 'D': 1, 'C': -3, 'Q': 3, 'E': 1, 'G': -2, 'H': 6, 'I': -2, 'L': -2, 'K': 0, 'M': -2,
          'F': -2, 'P': 0, 'S': -1, 'T': -1, 'W': -3, 'Y': 0, 'V': -2, 'B': 3, 'Z': 3},
    'I': {'A': -1, 'R': -2, 'N': -2, 'D': -2, 'C': -2, 'Q': -2, 'E': -2, 'G': -3, 'H': -2, 'I': 5, 'L': 2, 'K': -2,
          'M': 2, 'F': 1, 'P': -2, 'S': -1, 'T': 0, 'W': -5, 'Y': -1, 'V': 4, 'B': -1, 'Z': -1},
    'L': {'A': -2, 'R': -3, 'N': -3, 'D': -4, 'C': -6, 'Q': -2, 'E': -3, 'G': -4, 'H': -2, 'I': 2, 'L': 6, 'K': -3,
          'M': 4, 'F': 2, 'P': -3, 'S': -3, 'T': -2, 'W': -2, 'Y': -1, 'V': 2, 'B': -2, 'Z': -1},
    'K': {'A': -1, 'R': 3, 'N': 1, 'D': 0, 'C': -5, 'Q': 1, 'E': 0, 'G': -2, 'H': 0, 'I': -2, 'L': -3, 'K': 5, 'M': 0,
          'F': -5, 'P': -1, 'S': 0, 'T': 0, 'W': -3, 'Y': -4, 'V': -2, 'B': 2, 'Z': 2},
    'M': {'A': -1, 'R': 0, 'N': -2, 'D': -3, 'C': -5, 'Q': -1, 'E': -2, 'G': -3, 'H': -2, 'I': 2, 'L': 4, 'K': 0,
          'M': 6, 'F': 0, 'P': -2, 'S': -2, 'T': -1, 'W': -4, 'Y': -2, 'V': 2, 'B': -1, 'Z': 0},
    'F': {'A': -3, 'R': -4, 'N': -3, 'D': '-6', 'C': -4, 'Q': -5, 'E': -5, 'G': -5, 'H': -2, 'I': 1, 'L': 2, 'K': -5,
          'M': 0, 'F': '9', 'P': -5, 'S': -3, 'T': -3, 'W': 0, 'Y': 7, 'V': -1, 'B': -3, 'Z': -4},
    'P': {'A': 1, 'R': 0, 'N': 0, 'D': -1, 'C': -3, 'Q': 0, 'E': -1, 'G': 0, 'H': 0, 'I': -2, 'L': -3, 'K': -1, 'M': -2,
          'F': -5, 'P': 6, 'S': 1, 'T': 0, 'W': -6, 'Y': -5, 'V': -1, 'B': 1, 'Z': 1},
    'S': {'A': 1, 'R': 0, 'N': 1, 'D': 0, 'C': 0, 'Q': -1, 'E': 0, 'G': 1, 'H': -1, 'I': -1, 'L': -3, 'K': 0, 'M': -2,
          'F': -3, 'P': 1, 'S': 2, 'T': 1, 'W': -2, 'Y': -3, 'V': -1, 'B': 2, 'Z': 1},
    'T': {'A': 1, 'R': -1, 'N': 0, 'D': 0, 'C': -2, 'Q': -1, 'E': 0, 'G': 0, 'H': -1, 'I': 0, 'L': -2, 'K': 0, 'M': -1,
          'F': -3, 'P': 0, 'S': 1, 'T': 3, 'W': -5, 'Y': -3, 'V': 0, 'B': 2, 'Z': 1},
    'W': {'A': -6, 'R': 2, 'N': -4, 'D': -7, 'C': -8, 'Q': -5, 'E': -7, 'G': -7, 'H': -3, 'I': -5, 'L': -2, 'K': -3,
          'M': -4, 'F': 0, 'P': -6, 'S': -2, 'T': -5, 'W': 17, 'Y': 0, 'V': -6, 'B': -4, 'Z': -4},
    'Y': {'A': -3, 'R': -4, 'N': -2, 'D': -4, 'C': 0, 'Q': -4, 'E': -4, 'G': -5, 'H': 0, 'I': -1, 'L': -1, 'K': -4,
          'M': -2, 'F': 7, 'P': -5, 'S': -3, 'T': -3, 'W': 0, 'Y': 10, 'V': -2, 'B': -2, 'Z': -3},
    'V': {'A': 0, 'R': -2, 'N': -2, 'D': -2, 'C': -2, 'Q': -2, 'E': -2, 'G': -1, 'H': -2, 'I': 4, 'L': 2, 'K': -2,
          'M': 2, 'F': -1, 'P': -1, 'S': -1, 'T': 0, 'W': -6, 'Y': -2, 'V': 4, 'B': 0, 'Z': 0},
    'B': {'A': 2, 'R': 1, 'N': 4, 'D': 5, 'C': -3, 'Q': 3, 'E': 4, 'G': 2, 'H': 3, 'I': -1, 'L': -2, 'K': 2, 'M': -1,
          'F': -3, 'P': 1, 'S': 2, 'T': 2, 'W': -4, 'Y': -2, 'V': 0, 'B': 6, 'Z': 5},
    'Z': {'A': 1, 'R': 2, 'N': 3, 'D': 4, 'C': -4, 'Q': 5, 'E': 5, 'G': 1, 'H': 3, 'I': -1, 'L': -1, 'K': 2, 'M': 0,
          'F': -4, 'P': 1, 'S': 1, 'T': 1, 'W': -4, 'Y': -3, 'V': 0, 'B': 5, 'Z': 6}
}


def localAlignment(word1, word2, indelPenalty=5):

    # initialize nxm score matrix with zeros
    score_mat = [[0 for i in range(len(word2))] for j in range(len(word1))]

    #iterate through each letter of both strings
    for i in range(1, len(word1)):
        for j in range(1, len(word2)):
            if word1[i] in PAM250.keys():
                key1 = word1[i]
                key2 = word2[j]
            else:
                key1 = word2[j]
                key2 = word1[i]

            # get diagonal score + score of i,j in pam250
            score1 = score_mat[i - 1][j - 1] + PAM250[key1][key2]
            # get upper score - penalty
            score2 = score_mat[i - 1][j] - indelPenalty
            # get left score - penalty
            score3 = score_mat[i][j - 1] - indelPenalty
            # update the current cell with the max of the surrounding cells
            score_mat[i][j] = max(score1, score2, score3, 0)

    highScore = 0
    #iterate through score matrix to find max val
    for i in range(len(word1)):
        for j in range(len(word2)):
            if score_mat[i][j] > highScore:
                highScore = score_mat[i][j]
    return highScore


file = open('Input', 'r')
words = file.read().splitlines()
word1 = words[0]
word2 = words[1]

score = localAlignment(word1, word2)
print(score)
