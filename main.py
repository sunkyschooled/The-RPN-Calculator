print("Accepted Inputs:\nclr to Clear\nFloat or Integer\nOperator\np to Show Current Equation\nq to quit\n")
yee = 0  
equation = []
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
  booton = button
  if button.isnumeric() or isNumF(button):
    booton = float(button)
  if booton == "p":
    print(equation)
  elif booton == "q":
    quit()
  elif booton == "clr":
    while len(equation) > 0:
      equation.pop
  elif isNum(booton) == "nah" and len(equation) < 2:
    print("CRITICAL ERROR")
    quit() 
  elif isNum(booton) == "nah" and isOptr(booton) == "nah":
    print("CRITICAL ERROR")
    quit() 
  if isNum(booton) == "yah" or isOptr(booton) == "yah":
    equation.append(booton)
  if isNum(booton) == "nah" and len(equation) >= 3 and isOptr(booton) == "yah":
    equation.insert(0, RPN(equation.pop(), equation.pop(0), equation.pop(0)))
    print(equation[0])