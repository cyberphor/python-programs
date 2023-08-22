### Challenge 09
Someone wanted to play a joke on the incoming scholars on their first day at Bakery Square. Rather than just give them the floor number that the office is on, this person wrote instructions describing the absolute worst way to get here. The wild goose chase is structured as follows. There are only two types of directions in the instructions, up which is noted as ^ and down noted as v. Write a program that will read through the directions, however long they might be, and tell the poor scholars what floor they are supposed to end up on to get to the office.

**Assumptions** 
- The scholars all start on floor 0
- The building has infinitely many basement levels so they can travel as far down as the instructions tell them.
- The building has infinitely many stories so they can travel as far up as they are instructed.

**Sanity Checks**
- `v^v^v^v^` should result in floor 0
- `vv^^^^` should result in floor 2
- `^^vvvv` should result in floor -2
- `^^VA0vvvv` should result in floor -2

### Challenge 10
Visualize a scatter plot the perfect square roots of 1 through 100.

### Challenge 11
Add first 10 triangle numbers of last scatter plot to scatter plot. 

### Challenge 12
Implement the "bisection method" (i.e., find the square root of a function) and solve for the following:
```
a = 0
b = 3
def f(x)
    e = cos(x) - 0.5
    return e
max_iters = 100
answer = 2.3349609
```

The Bisection Method
1. Start with an interval [a, b] that contains a root (i.e., the function changes sign)
2. Compute the midpoint 
3. If the function at c is zero then,
    c is the solution and the algorithim stops
4. Else the solution must be within the interval
    If the function at a and c have opposite signs,
        the root is within [a, c]
    If the function at c and b have opposite signs
        the root is within [c, b]
5. Repeat with the new interval
6. Stop once a pre-defined number of interations