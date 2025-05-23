import math
from math import sin,cos,sqrt,pow,pi,exp
def run_numint() :
    print("")
    print("Enter the function :")
    eqn = input()
    
    print("Enter a:")
    a = input()
    print("Enter b:")
    b = input()

    if '.' in a:
        a = float(a)
    else:
        a = int(a)

    if '.' in b:
        b = float(b)
    else:
        b = int(b)

    t = evalEqn(((a+b)/2),eqn)

    midpoint = (b-a) * t

    print("Midpoint : " + str(midpoint))

    trapezoidal = (b-a) * (evalEqn(a,eqn) + evalEqn(b,eqn))/2

    print("Trapezoidal : " + str(trapezoidal))

    simpson = ((b-a)/6) * (evalEqn(a,eqn)+ (4*t) + evalEqn(b,eqn))

    print("Simpson : " + str(simpson))

def evalEqn(x,eqn):
    e = eval(eqn)
    return e