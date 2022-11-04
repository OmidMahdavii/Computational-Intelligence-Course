# Lab 2

### Task

Given a number ***N*** and some lists of integers ***P = (L<sub>0</sub>, L<sub>1</sub>, L<sub>2</sub>, ..., L<sub>n</sub>)***,  determine, if possible, ***S = (L<sub>S0</sub>, L<sub>S1</sub>, L<sub>S2</sub>, ..., L<sub>Sn</sub>)*** such that each number between ***0*** and ***N - 1*** appears in at least one list.

### Final Results

Solution for N=5: Weight: 5

Solution for N=10: Weight: 10

Solution for N=20: Weight: 23

Solution for N=50: Weight: 85

Solution for N=100: Weight: 186

Solution for N=500: Weight: 1369

### Algorithm Description

The problem contains a list containing several inner lists with different lengths. I'd rather determine the parameters dependent on the ***N*** since the list size is variable with respect to ***N***. Population size is ***5N***, offspring size is ***2N***, and the number of generations is ***50N***.

In the algorithm, each genome is a list containing boolean elements equal to the length of the main list. A `True` value in each index means that the corresponding solution contains the list with the same index. Moreover, fitness is defined using a `tuple` containing two parameters. The first criterion demonstrating the fitness of a solution is the number of elements of the goal set that are missing in the solution. The other parameter is the total elements in the solution. Thereby, in this algorithm, the intention is to minimize the fitness of the population (in other words, it could be perceived that the fitness is defined so: `(-i.missing, -i.weight)`). Furthermore, in the evolution process, the offspring is produced only by mutation and since the cross-over approach does not seem helpful, it has not been utilized.