import sys


class Node:
    def __init__(g, key):
        g.key = key
        g.age = 0


class Graph:
    def __init__(g):
        g.nodes = {}
        g.edges = []


def UPGMA(D, n):
    g = Graph()
    distanceDict = {}
    # form dictionary representation of matrix
    # each key is an int from 0 - n-1
    for i in range(len(D)):
         # each value is another dict 
        distanceDict[i] = {}
        # key = row, value = column
        for j in range(len(D[i])):
            distanceDict[i][j] = D[i][j]

    # n single element clusters keyed 1 to n
    Clusters = {}
    for i in range(n):
        Clusters[i] = [i]

    # n nodes keyed by single elements 1 to n
    for i in range(n):
        if i in g.nodes:
            newNode = g.nodes[i]
        node = Node(i)
        g.nodes[i] = node
        newNode = node

    newKey = n
    T = []
    # while more than one cluster
    while len(distanceDict) > 1:
        minDistance = float("Inf")
        nodes = list(distanceDict.keys())
        # find the two closest clusters
        for i in range(n - 1):
            for j in range(i + 1, len(nodes)):
                if distanceDict[nodes[i]][nodes[j]] < minDistance:
                    minDistance = distanceDict[nodes[i]][nodes[j]]
                    # index of current min distance
                    newIndex1 = nodes[i]
                    newIndex2 = nodes[j]


        # merge close clusters into new cluster 
        newCluster = Clusters[newIndex1] + Clusters[newIndex2]

        # add newCluster node to T
        if newKey in g.nodes:
            newNode = g.nodes[newKey]
        node = Node(newKey)
        g.nodes[newKey] = node
        newNode = node
        T.append([newKey, newIndex1])
        T.append([newKey, newIndex2])

        newNode.age = distanceDict[newIndex1][newIndex2] / 2
        # connect newCluster to merged indexes
        distanceDict[newKey] = {}
        distanceDict[newKey][newKey] = 0
        for previousNode in nodes:
            total = 0
            count = 0
            #add to rows/cols to distanceDict
            for initNode in Clusters[previousNode]:
                for node in newCluster:
                    total = total + D[initNode][node]
                    count = count + 1
                    
            distanceDict[previousNode][newKey] = total / count
            distanceDict[newKey][previousNode] = total / count

        Clusters[newKey] = newCluster
        newKey = newKey + 1

        # remove rows and columns of D corresponding to cluster
        for key in distanceDict.keys():
            del distanceDict[key][newIndex1]
        for key in distanceDict.keys():
            del distanceDict[key][newIndex2]

        # remove cluster indexes from cluster
        del distanceDict[newIndex1]
        del distanceDict[newIndex2]

    # for edge in tree
    for edge in T:
        # length of edge v to w is age(v) - age(w)
        length = g.nodes[edge[0]].age - g.nodes[edge[1]].age
        g.edges.append(edge + [length])
        g.edges.append(edge[::-1] + [length])

    g.edges.sort()
    # return T
    return g.edges


with open('input.txt') as input:
    rawInput = input.read().splitlines()
    n = int(rawInput[0])
    D= [[int(x) for x in line.split()] for line in rawInput[1:]]
    adjacencyMatrix = UPGMA(D, n)

    for x, y, weight in adjacencyMatrix:
        print( str(x) + '->' + str(y) + ':' + str(round(weight, 3)))