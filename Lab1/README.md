# Lab 1

#### Task

Given a number ***N*** and some lists of integers ***P = (L<sub>0</sub>, L<sub>1</sub>, L<sub>2</sub>, ..., L<sub>n</sub>)***,  determine, if possible, ***S = (L<sub>S0</sub>, L<sub>S1</sub>, L<sub>S2</sub>, ..., L<sub>Sn</sub>)*** such that each number between ***0*** and ***N - 1*** appears in at least one list.

#### Final Results

Solution for N=5: Weight: 5, Nodes visited: 2

Solution for N=10: Weight: 10, Nodes visited: 8

Solution for N=20: Weight: 23, Nodes visited: 193

Solution for N=50: Weight: 70, Nodes visited: 1738

Solution for N=100: Weight: 167, Nodes visited: 4199

Solution for N=500: Weight: , Nodes visited: 

Solution for N=1000: Weight: , Nodes visited:

#### Algorithm Description

The problem contains a list containing several inner lists with different lengths. In the beginning, one inner list is extracted. Then it is checked if the same list has been analyzed before (in case of similar inner lists). After that, the selected inner list is added to the (empty) state and an ad-hoc sort is implemented on the outer list. First, the list is sorted by the increasing number of common elements with the state. In case of an equal number of common elements, the list with a larger length goes first. I believe that this algorithm helps to find the minimum weight sooner. Then a recursive function is called for each state. The function compares the current state with the goal state and compares the weight with the minimum weight so far in case of success. Otherwise, the first element from the sorted outer list is popped and appended to the state and the function is called again. 

Furthermore, several bounds have been considered for the problem to limit the computation. Whenever we reach a depth equal to the ***N***, it means that we achieved the ideal answer and the process is stopped. On the other hand, the worst case of the state in order to be equal to the goal is the situation in which there are ***N*** elements in the state. Therefore if the length of the state is larger, the branch is trimmed. The other constraint is the number of common elements between the state and the list-to-be-appended. If the number is equal to the unique values in the state, it means that this path is not going to show us the solution.