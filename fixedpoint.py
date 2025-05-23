from tabulate import tabulate
import math

def getFx(x):
    
    return pow(x,2) - 3

def getGx(x):
    
    return pow(x,2) - 3 + x

def fixedPointIteration(x0, tol, max_iterations):
    
    x_i = x0
    rows = []

    for i in range(1, max_iterations + 1):
        g_x_i = getGx(x_i)
        f_x_i = getFx(x_i)
        difference = abs(g_x_i - x_i)
        
        row = [i, x_i, f_x_i, g_x_i, difference, difference < tol, i == max_iterations]
        rows.append(row)

        if difference < tol:
            print(tabulate(rows, headers=['i', 'x_i', 'f(x_i)', 'g(x_i)', '|g(x_i) - x_i|', '|g(x_i) - x_i| < tol', 'i == N']))
            print(f"\nApprox Root: {g_x_i}")
            return

        x_i = g_x_i

    print(tabulate(rows, headers=['i', 'x_i', 'f(x_i)', 'g(x_i)', '|g(x_i) - x_i|', '|g(x_i) - x_i| < tol', 'i == N']))
    print("\nMaximum iterations reached. No solution found within tolerance.")

# Initial guess, tolerance, and maximum number of iterations
x0 = 1
tol = 0.01
max_iterations = 5

# Execute the Fixed-Point Iteration method
def solve():
   x0 = 1
   tol = 0.01
   max_iterations = 5
   fixedPointIteration(x0, tol, max_iterations)