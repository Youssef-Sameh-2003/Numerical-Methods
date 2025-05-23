import linreg, numint, composite, newdivdif, bisection, secant, modsecant, newtraph, fixedpoint


class bcolor:
    FAIL = '\033[91m'
    ENDC = '\033[0m'

print("Numerical Method Project | v1.0\n")
print("By Yusuf Sameh\n")
print("* Notes *")
print("- sqrt(x) ---> Square Roots")
print("- pow(a,b)--- > Power a^b")
print("- pi ---> For Math PI")
print("- exp(x) ---> For e^x\n")

print ("Choose a method :")
print("[1] Linear Regression")
print("[2] Numerical Integration")
print("[3] Composite")
print("[4] Newton Divided Difference")
print("[5] Bisection Method")
print("[6] Secant Method")
print("[7] Modified Secant")
print("[8] Newton Raphson")
print("[9] Fixed Point\n")

choice = int(input("Choose 1 ~ 9 : "))

if choice == 1 :
     linreg.run_linreg()

elif choice == 2 :
     numint.run_numint()

elif choice == 3 :
     composite.run_composite()

elif choice == 4 :
     newdivdif.run_newdivdif()

elif choice == 5:
     bisection.SolveEqn()

elif choice == 6:
     secant.check_solvable()

elif choice == 7:
     modsecant.check_solvable()

elif choice == 8:
     newtraph.solve()

elif choice == 9:
     fixedpoint.solve()

else:
   print("Invalid input")
