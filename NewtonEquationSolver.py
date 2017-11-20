import math
h=0.0001 # step for derivative
iterations = 10
x=float(-0.4) # first iteration X0 value 

def f(x): # function to iterate
    return (pow(x,3)-2*pow(x,2)+1)

# page 55 Aplied Numerical Methods Simonyan
def f_1(x):
    return (-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h)
def f_2(x):
    return (2*f(x)-5*f(x+h)+4*f(x+2*h)-f(x+3*h))/pow(h,2)
def f_3(x):
    return (-5*f(x)+18*f(x+h)-24*f(x+2*h)+14*f(x+3*h)-3*f(x+4*h))/(2*pow(h,3))

# page 164 Aplied Numerical Methods Simonyan
# Newton's method solving f(x) = 0
def first(x):
    for i in range(iterations):
        print(x)
        x = x - (f(x)*f_1(x))/(pow(f_1(x),2)-0.5*f(x)*f_2(x))
def seccond(x):
    for i in range(iterations):
        print(x)
        x = x - (f(x)*pow(f_1(x),2) - 0.5*pow(f(x),2)*f_2(x)) / (pow(f_1(x),3) - f(x)*f_1(x)*f_2(x) + (pow(f(x),2)*f_3(x))/6)
def third(x):
    for i in range(iterations):
        print(x)
        x = x - ( f(x) * pow(f_1(x),2) - 0.5*pow(f(x),2) * f_2(x) ) / ( pow(f_1(x),3) )
def fourth(x):
    for i in range(iterations):
        print(x)
        x = x - ((f(x) * pow(f_1(x),2) + 0.5*pow(f(x),2) * f_2(x)) / (pow(f_1(x),3))) + (pow(f(x),3)*(f_1(x)*f_3(x)-3*pow(f_2(x),2))/(6*pow(f_1(x),5)))
def double(x):
    for i in range(iterations):
        print(x)
        x=x-f_1(x)/f_2(x)

first(x)
print(" ")
seccond(x)
print(" ")
third(x)
print(" ")
fourth(x)
print(" ")