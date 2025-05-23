import math
from math import sin,cos,sqrt,pow,pi,exp

def run_composite() :
    print("")
    print("Enter the function :")
    eqn = input()
    
    print("Enter a:")
    a = input()
    print("Enter b:")
    b = input()
    print("Enter h:")
    h = input()

    

    if '.' in a:
        a = float(a)
    else:
        a = int(a)

    if '.' in b:
        b = float(b)
    else:
        b = int(b)

    if '.' in h:
        h = float(h)
    else:
        h = int(h)

    mid = find_midpoint(a,h)

    x = [0]*5
    fx = [0]*5
    sfx = 0
    cmp = 0

    calc_cmp_midpoint(x,fx,sfx,mid,h,eqn)

    calc_cmp_trapezoidal(x,fx,sfx,h,eqn)

    calc_cmp_simpson(sfx,h,eqn)

def calc_cmp_simpson(sfx,h,eqn):
    x = [0]*6
    fx = [0]*6
    x[0] = 0

    for n in range(5):
        x[n+1] += x[n] + h

    for n in range(len(x)-1):
        fx[n] = evalEqn(x[n],eqn)

    for n in range(len(fx)):
        sfx += fx[n]

    cmp_simpson = (h/3) * (fx[0] + 4*fx[1] + 2*fx[2] + 4*fx[3] + fx[4])

    print("Composite Simpson : " + str(cmp_simpson))

def calc_cmp_trapezoidal(x,fx,sfx,h,eqn):
    x = [0]*6
    fx = [0]*6
    x[0] = 0
    
    for n in range(5):
        x[n+1]+= x[n] + h

    for n in range(len(x)-1):
        fx[n] = evalEqn(x[n],eqn)

    for n in range(1, len(fx)-2):
        sfx += fx[n]

    cmp_trap = h/2 * (fx[0] + 2*sfx + fx[len(fx)-2])
    print("Composite Trapezoidal : " + str(cmp_trap))
   
def calc_cmp_midpoint(x,fx,sfx,mid,h,eqn):
    x[0] = mid

    for n in range(4):
        x[n+1] += x[n] + h
        
    for n in range(len(x)-1):
        fx[n] = evalEqn(x[n],eqn)

    for n in range(len(fx)):
        sfx += fx[n]
        
    cmp = sfx * h
    print("Composite Midpoint : " + str(cmp))

def find_midpoint(a,h):
    mid = (a +h)/2
    return mid

def evalEqn(x,eqn):
    e = eval(eqn)
    return e