import random
import itertools
from functools import reduce

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]


def findCommonElements(a: set, b: list):
    commonElements = 0
    for element in a:
        if element in b:
            commonElements += 1
    return commonElements


def listToSet(L):
    return set(itertools.chain([element for sublist in L for element in sublist]))


def adHocSort(state, lists):
    return sorted(lists, key=lambda x: (findCommonElements(state, x), -len(x)))


def computeWeight(lists: list):
    return reduce(lambda x, y: x + len(y) if isinstance(x, int) else len(x) + len(y), lists)


def mySolution(n, state, goalState, lists):
    global minWeight, finalList, totalNodes 
    sortedLists = adHocSort(listToSet(state), lists)
    if len(state) >= n or sortedLists[0] in state:
        return
    totalNodes += 1
    state.append(sortedLists[0])
    if listToSet(state) == goalState:
        weight = computeWeight(state)
        if minWeight is None or weight < minWeight:
            minWeight = weight
            finalList = state
        return
    else:
        newLists = sortedLists[1:]
        mySolution(n, state, goalState, newLists)
    return


if __name__ == '__main__':
    n = 100
    myLists = problem(n, 42)
    goalState = set(range(n))
    minWeight = None
    totalNodes = 0
    finalList = []
    analyzedLists = []
    for l in myLists:
        if l in analyzedLists:
            continue
        analyzedLists.append(l)
        state = []
        state.append(l)
        sortedLists = adHocSort(listToSet(state), myLists)
        mySolution(n, state, goalState, sortedLists)
        if minWeight == n:
            break
    # print(finalList)
    print(f'Weight: {minWeight}, Nodes visited: {totalNodes}')




