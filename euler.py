#Erik Hansen and Gary Li
#6/7/18
#Calculus Euler's Method

from math import *
print('If sinx function, input it as sin(x)')
print('If cosx function, input it as cos(x)')
print('If tanx function, input it as tan(x)')
print('If cotx function, input it as 1/tan(x)')
print('If secx function, input it as 1/cos(x)')
print('If cscx function, input it as 1/sin(x)')
print('If inverse sin(x) function, input it as asin(x)')
print('If inverse cos(x) function, input it as acos(x)')
print('If inverse tan(x) function, input it as atan(x)')
print('If inverse cot(x) function, input it as acot(x)')
print('If inverse sec(x) function, input it as asec(x)')
print('If inverse csc(x) function, input it as acsc(x)')
print('If lnx function, input it as log(x)')
print('If e^x function, input it as exp(x)')
print('If a^x function, input it as pow(a,x)')
print('Input x^ as x**')
print('Use the * to show multiplication. Ex: 3x^2 is 3*x**2')

derivative = input("Input f'(x): ")
y = float(input("Input the y-value: "))
x = float(input("Input the x-value: "))
xapprox = float(input("Input the x-value you wish to approximate: "))
steps = int(input("Input the number of steps between approximate value and the original x: "))
dx= (xapprox-x)/steps

if xapprox>=x:
    while x <= xapprox:
        for i in range(1,steps+1):
            dydx = float(eval(derivative))
            dy= dydx*dx
            x+=dx
            y+=dy
else:
    while x >= xapprox:
        for i in range(1,steps+1):
            dydx = float(eval(derivative))
            dy= dydx*dx
            x+=dx
            y+=dy

print('The approximated point is','(',x,',',y,')')