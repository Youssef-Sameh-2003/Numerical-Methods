import math
from tabulate import tabulate

def getFx(x): 
    return pow(x,2) - 3

def getFPrimeX(x):    
    return 2*x 

def newtonRaphson(x0, tol, max_iterations):
    x_i = x0
    rows = []

    for i in range(1, max_iterations + 1):
        f_x_i = getFx(x_i)
        f_prime_x_i = getFPrimeX(x_i)
        
        if f_prime_x_i == 0:
            print("Derivative is zero. No solution found.")
            return

        x_i_plus_1 = x_i - f_x_i / f_prime_x_i
        difference = abs(x_i_plus_1 - x_i)
        
        row = [i, x_i, f_x_i, f_prime_x_i, x_i_plus_1, difference, difference < tol, i == max_iterations]
        rows.append(row)

        if difference < tol:
            print(tabulate(rows, headers=['i', 'x_i', 'f(x_i)', 'f\'(x_i)', 'x_{i+1}', '|x_{i+1} - x_i|', '|x_{i+1} - x_i| < tol', 'i == N']))
            print(f"\nApprox Root: {x_i_plus_1}")
            return

        x_i = x_i_plus_1

    print(tabulate(rows, headers=['i', 'x_i', 'f(x_i)', 'f\'(x_i)', 'x_{i+1}', '|x_{i+1} - x_i|', '|x_{i+1} - x_i| < tol', 'i == N']))
    print("\nMaximum iterations reached. No solution found within tolerance.")

# Initial guess, tolerance, and maximum number of iterations
x0 = 1
tol = 0.01
max_iterations = 4

# Execute the Newton-Raphson method
def solve():
  x0 = 1
  tol = 0.01
  max_iterations = 4
  newtonRaphson(x0, tol, max_iterations)