import math
from tabulate import tabulate
from math import sin,cos,sqrt,pow,pi,exp

rows = []

def getFx(x,eqn):
    e = eval(eqn)
    return e


def SolveEqn():
    
    print("Enter the function :")
    eqn = input()

    print("Enter a:")
    a = int(input())

    print("Enter b:")
    b = int(input())

    c = (a + b) / 2

    print("Enter tolerance:")
    tol = float(input())

    #Number of iterations
    N = (math.log2((b -a)/tol))/math.log2(2)

    # Custom rounding logic
    decimal_part = N - int(N)

    if decimal_part < 0.5:
     N = math.floor(N)  # Round down
    else:
     N = math.ceil(N)   # Round up


    fa = getFx(a,eqn)
    fb = getFx(b,eqn)
    
    if(check_solvable(fa,fb)):
       fc = getFx(c,eqn)
    else:
       print("This Equation is not solvable")

    i = 1
    lttol = False
    ien = False
    for i in range(1, int(N)+1):
      if(abs(fc) < tol):
       lttol = True
    
      if(i == N):
       ien = True

      row = [i, a, b, c, fa, fb, fc, lttol, ien]
      rows.append(row)

      if(ien == True or lttol == True):
       break

      if fc < 0:
        fa = fc
        a = c

      if fc > 0:
        fb = fc
        b = c

      c = (a + b) / 2
      fc = getFx(c,eqn)

    print(tabulate(rows, headers=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', 'f(c) < tol', 'i == N']))
    print("")
    print("Approx Root : " + str(c))



    

def check_solvable(fa,fb):
    
    if(fa * fb > 0):
        return False
    else:       
        return True

