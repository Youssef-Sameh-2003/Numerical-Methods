def run_linreg() :
  print("")
  print("Points of X`: ")
  xp = input().rsplit(',')

  print("Points of Y`: ")
  yp = input().rsplit(',')

  print("Enter value of x: ")
  x = float(input())

  
  if len(xp) != len(yp):
      print("X and Y must be same size !!!")
  else:
      n = len(xp)
      sxy = 0
      sx = 0
      sy = 0
      sx2 = 0
      for i in range(n):

        if '.' in xp[i]:
           xp[i] = float(xp[i])
        else:
           xp[i] = int(xp[i])

        if '.' in yp[i]:
           yp[i] = float(yp[i])
        else:
           yp[i] = int(yp[i])

        sxy = sxy + (xp[i] * yp[i])
        sx = sx + xp[i]
        sy = sy + yp[i]
        sx2 = sx2 + pow(xp[i],2)

      a = (n*sxy-sx*sy)/(n*sx2-pow(sx,2))

      b = (sy)/n - (a * sx)/n

      y = a * x + b


      print("a: " + str(a))
      print("b: " + str(b))
      print("")
      print("Linear Regression (y) = ")
      print(y)
