print("Accepted Inputs:\nclr to Clear\nFloat or Integer\nOperator\np to Show Current Equation\nq to quit\ni to invert\nn to negate")
yee = 0  
def RPN(c,a,b):
  if c == "+":
    return (a+b)
  if c == "-":
    return (a-b)
  if c == "/":
    return (a+b)
  if c == "*":
    return (a*b)
  if c == "^":
    return (a**b)
  if c == "root":
    return (a**(1/b))
def isNum(x):
  if isinstance(x,int):
    return "yah"
  elif isinstance(x,float):
    return "yah"
  else:
    return "nah"
def isOptr(x):
  if x == "+":
    return "yah"
  elif x == "-":
    return "yah"
  elif x == "/":
    return "yah"
  elif x == "*":
    return "yah"
  elif x == "^":
    return "yah"
  elif x == "root":
    return "yah"
  else:
    return "nah"
def isNumF(x):
  try:
      float(x)
      return True
  except ValueError:
      return False
while yee != 1:
  button = (input(""))
  inputlist = button.split()
  equation = []
  for x in range(0, len(inputlist)):
    booton = inputlist[x]   
    if inputlist[x].isnumeric() or isNumF(inputlist[x]):
      equation.append(float(inputlist[x]))
    if booton == "p":
      print(equation)
    elif booton == "q":
      quit()
    elif booton == "i":
      equation.append(1/(equation.pop()))
    elif booton == "n":
      equation.append(-1*equation.pop())
    elif booton == "clr":
      while len(equation) > 0:
        equation.pop()
    if isOptr(booton) == "yah":
      equation.append(RPN(booton, equation.pop(), equation.pop()))
  print(equation[0])