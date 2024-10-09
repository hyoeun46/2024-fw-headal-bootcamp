def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def solve_factorial(n):
    print(factorial(n))

n = int(input())
solve_factorial(n)