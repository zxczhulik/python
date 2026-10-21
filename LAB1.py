import math
def HelloWorld(a: str):
    print('HelloWorld!')

def ExpX(x: float, eps: float)-> float:
    sum = 1.0
    term = 1
    n = 1       

    while abs(term) > eps:
        term = term*x/n
        sum += term
        n += 1
    
    return sum

def ExpMX(x: float, eps: float)-> float:
    sum = 1.0
    term = 1
    n = 1       

    while abs(term) > eps:
        term = term*(-x)/n
        sum += term
        n += 1
    
    return sum

def cos(x: float, eps: float)-> float:
    sum = 1.0
    term = 1
    n = 1

    while abs(term) > eps:
        term = term*(-x*x)/((2*n-1)*2*n)
        sum += term
        n += 1
    
    return sum

def ln(x: float, eps: float)-> float:
    if x > 1 or x <= -1: return
    term = -x
    sum = term
    n = 1

    while abs(term) > eps:
        n += 1
        term = term * x * (n - 1) / n
        sum += term

    return sum

x = float(input("input x: "))
eps = float(input("input epsilon: "))


print(ExpX(x, eps))
print(ExpMX(x, eps))
print(cos(x, eps))
print(ln(x, eps))
HelloWorld('print')