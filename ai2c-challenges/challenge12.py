from numpy import exp, cos

def samesign(a, b):
    return a * b > 0

def f(x):
    return exp(cos(x)) - 0.5

def solution(a: int, b: int, f, max_interval: int):
    for i in range(max_interval):
        assert not samesign(f(a), f(b))
        c = (a + b) / 2
        if c == 0:
            return c
        if f(a) * f(b) > 0:
            a = c
        else:
            b = c
        print(c)
    return c

if __name__ == "__main__":
    """
    1. Start with an interval [a, b] that contains a root (i.e., the function changes sign)
    2. Compute the midpoint 
    3. If the function at c is zero then,
        c is the solution and the algorithim stops
    4. Else the solution must be within the interval
        If the function at a and c have opposite signs,
            the root is within [a, c]
        If the function at c and b have opposite signs
            the root is within [c, b]
    """
    solution(a = 0, b = 3, f = f, max_interval = 100)