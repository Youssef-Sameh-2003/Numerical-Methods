import math
from tabulate import tabulate

rows = []

def getFx(x):
    Fx = pow(x,2) - 3
    return Fx


def SolveEqn():
 a = 1; b = 2

 tol = 0.01

 #Number of iterations
 N = (math.log2((b -a)/tol))/math.log2(2)

 # Custom rounding logic
 decimal_part = N - int(N)
 if decimal_part < 0.5:
    N = math.floor(N)  # Round down
 else:
    N = math.ceil(N)   # Round up

 fa = getFx(a)
 fb = getFx(b)

 c = b - fb * ((b-a)/(fb - fa))
 fc = getFx(c)

 
 i = 1
 lttol = False
 ien = False

 print("f(x) = x^2-3")
 print("a = 2, b = 5")
 print("tol = 0.01")
 print("N = " + str((N)))
 print("")
 for i in range(1, int(N)+1):
  if(abs(fc) < tol):
   lttol = True
    
  if(i == N):
    ien = True

  row = [i, a, b, c, fa, fb, fc, lttol, ien]
  rows.append(row)

  if(ien == True or lttol == True):
      break;

  ''' if fc < 0:
    fa = fc
    a = c

  if fc > 0:
    fb = fc
    b = c
 '''

  fa = fb
  fb = fc
  a = b
  b = c


  c = b - fb * ((b-a)/(fb - fa))
  fc = getFx(c)

 print(tabulate(rows, headers=['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', 'f(c) < tol', 'i == N']))
 print("")
 print("Approx Root : " + str(c))

def check_solvable():
    a = 1; b = 2
    fa = getFx(a)
    fb = getFx(b)
    if(fa * fb > 0):
        print("Not Solvable !!!")
    else:
        SolveEqn()

