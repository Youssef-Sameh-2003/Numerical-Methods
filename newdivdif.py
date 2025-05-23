import math
from math import sin, cos, sqrt, pow, pi, exp

def run_newdivdif():
  print("")
  print("Points of X`: ")
  xp = input().rsplit(',')

  print("Enter the function :")
  eqn = input()

  fx = [0]*len(xp)
  fxcal = [0]*(len(xp)-1)
  fxcal2 = [0]*(len(xp)-2)
  fxcal3 = [0]*(len(xp)-3)

  for i in range(len(xp)):
    if '.' in xp[i]:
      xp[i] = float(xp[i])
    elif 'pi' in xp[i]:
      xp[i] = float(eval(xp[i]))
    else:
      xp[i] = int(xp[i])

  for i in range(len(xp)):
     fx[i] = evalEqn(xp[i], eqn)


  # First divided difference
  for i in range(len(xp)-1):
    fxcal[i] = (fx[i+1] - fx[i])/(xp[i+1] - xp[i])

  # Second divided difference
  for i in range(len(xp)-2):
        fxcal2[i] = (fxcal[i+1] - fxcal[i])/(xp[i+2] - xp[i])
  # Third divided difference
  for i in range(len(xp)-3):
        fxcal3[i] = (fxcal2[i+1] - fxcal2[i])/(xp[i+3] - xp[i])

  print("First divided difference : ")
  for n in range(len(fxcal)):
    print("{:.2f}  ".format(fxcal[n]), end="")

  print("\nSecond divided difference : ")
  for n in range(len(fxcal2)):
     print("{:.2f}  ".format(fxcal2[n]), end="")




  if (len(xp) == 4):
    print("\nThird divided difference : ")
    for n in range(len(fxcal3)):
      print("{:.2f}\n".format(fxcal3[n]), end="")

    print("P(X)= " + str(fxcal[0]) + " + " + "{:.2f}".format((fxcal[0])) + "(x-" + "{:.2f}".format(xp[0]) + ")" + " + " + "{:.2f}".format(fxcal2[0]) + "(x-" + "{:.2f}".format(xp[0])+ ")"+ "(x-" + "{:.2f}".format(xp[1])+ ")" + " + " + "{:.2f}".format(fxcal3[0]) + "(x-" + "{:.2f}".format(xp[0])+ ")" + "(x-" + "{:.2f}".format(xp[1])+ ")" + "(x-" + "{:.2f}".format(xp[2]) + ")" )
  
  else:
    print("\nP(X)= " + str(fxcal[0]) + " + " + "{:.2f}".format((fxcal[0])) + "(x-" + "{:.2f}".format(xp[0]) + ")" +" + "+ "{:.2f}".format(fxcal2[0]) + "(x-" + "{:.2f}".format(xp[0])+ ")"+ "(x-" + "{:.2f}".format(xp[1])+ ")")
  


def evalEqn(x,eqn):
    e = eval(eqn)
    return e