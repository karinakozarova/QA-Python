def f_c(x):
    # returns the constant 4 for any given input
    return 4

def f_x(x, a, b):
    res = (a*x) + b
    return res

def sum(x):
  return f_x(x, 1, 1)+ f_x(x, 2, 2)+ f_x(x, 3, 3)
