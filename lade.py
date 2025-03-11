# Euler method is a method that convert differnetial equation into an ordinary differential equation.
import math
def euler_method(x,y,eq,h,n):
    e=math.exp(1)
    x=x
    y=y

    for i in range(n):
        y_ = y+h*(eval(eq))
        x_= x+h
        y = y_
        x = x_
        
        print(f'Iteration Number {i+1} : y{i+1}={y} \t x{i+1}={x}')

x = int(input('Enter first value of x:'))
y = int(input('Enter first value of y:'))
h = float(input('Enter the step size:'))
n = int(input('Enter the total number of iteration:'))
eq= input('Enter the differential equation:')

euler_method(x,y,eq,h,n)


