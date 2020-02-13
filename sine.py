import math

def sin(x):
    if x > 360:
        x = x%360
        print(x)
    x = x/180*math.pi
    term = x
    sum = x
    eps = 1E-8
    n = 2
    while abs(term/sum) > eps:
        term = -(term*x*x)/(((2*n)-1)*((2*n)-2))
        sum = sum + term
        n += 1
    return sum
        
print(sin(3000))

x = (float(input("Enter an angle in degrees: ")))
result = math.sin(x/180*math.pi)
print("sin(x) = ", result)
