import random
from functools import reduce
from time import perf_counter_ns
import logging

logging.basicConfig(level=logging.INFO)

minWeight = None
totalNodes = 0
finalList = []


def problem(N, seed=None):
    random.seed(seed)
    return [
        list(
            set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2)))
        )
        for n in range(random.randint(N, N * 5))
    ]


# more efficient to use sets properties like intersection
# instead of for loop with checks
def findCommonElements(a: set, b: list):
    return len(a.intersection(b))


# don't need itertools to convert to a set
def listToSet(L):
    return set(element for sublist in L for element in sublist)


def adHocSort(state, lists):
    return sorted(lists, key=lambda x: (findCommonElements(state, x), -len(x)))


def computeWeight(lists: list):
    return reduce(
        lambda x, y: x + len(y) if isinstance(x, int) else len(x) + len(y), lists
    )


# probably you don't need recursion
# and it is better to use iteration
# which is less computational intense
def mySolution(n, state, goalState, lists):
    global minWeight, finalList, totalNodes
    # declare theme globally instead
    sortedLists = adHocSort(listToSet(state), lists)
    # >= n should be > n
    # because a solution with n lists could still be an optimal solution
    # n = 3 ==> sol = [[0],[1],[2]] ==> len(sol) == 3
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
    # don't need else after return
    newLists = sortedLists[1:]
    mySolution(n, state, goalState, newLists)
    return


if __name__ == "__main__":
    start = perf_counter_ns()
    n = 10
    myLists = problem(n, 42)
    goalState = set(range(n))
    analyzedLists = []
    for l in myLists:
        if l not in analyzedLists:
            analyzedLists.append(l)
            state = [l]
            sortedLists = adHocSort(set(l), myLists)
            mySolution(n, state, goalState, sortedLists)
            if minWeight == n:
                break
    end = perf_counter_ns()
    logging.info(f"Weight: {minWeight}, Nodes visited: {totalNodes}")
    logging.debug(f"time elapsed : {end - start} ns")
