import math
h=0.0001 # step for derivative
iterations = 10


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
        x = x - f_1(x)/f_2(x)
        #print("f_1 = " ,i,"  ", f_1(x))
        #print("f_2 =  ",i,"  ", f_2(x))
        #break
def fixed_right_edge_chord(b,x): #fixed with right edge chord method "quasi-Newton method" 167 Simonyan
    if (f(b)*f_2(b) > 0):
        print("yes")
    else:
        return 0
    for i in range(iterations):
        x = x - ((b-x)*f(x))/(f(b)-f(x))
        print(x)

def fixed_left_edge_chord(a, x):  #fixed with left edge chord method "quasi-Newton method" 167 Simonyan
    if (f(a) * f_2(a) > 0):
        print("yes")
    else:
        return 0
    for i in range(iterations):
        x = x - ((a - x) * f(x)) / (f(a) - f(x))
        print(x)
def combination(a,b):# page 167
    x = a
    __x__= b
    if (f(a) * f_2(a) > 0):
        print("yes")
    else:
        return 0
    #print("x")
    for i in range(iterations):
        #x = x - f(x)/f_1(x)
        __x__ = x - ((__x__-x)*f(x))/(f(__x__)-f(x))
        #print(__x__)
    print("__x__")
    for i in range(iterations):
        x = x - f(x)/f_1(x)
        print(x)

def basic_iteration_system_solver(x,y):
    for i in range(iterations):
        print(x, '\t', y)
        y_=y
        y = pow(x, 2) + 5
        x = (y_/2)-2


x=0.2
print("f(x)=pow(x,3)-2*pow(x,2)+1 , x=0.2")

print("առաջին")
first(x)
print(" ")
print("երկրորդ")
seccond(x)
print(" ")
print("երրորդ")
third(x)
print(" ")
print("չորրորդ")
fourth(x)
print(" ")


a = -1
b = 2
x = -0.5
print("a = -1,b = 2,x = -0.5 ")
print("անշարժ աջ եզրով լարերի մեթոդով")
if fixed_right_edge_chord(b,x) == 0:
    print("error right_edge")
print(" ")
print("անշարժ ձախ եզրով լարերի մեթոդով")
if fixed_left_edge_chord(b,x) == 0:
    print("error right_edge")

print(" ")
print("զուգակցման մեթոդ")
combination(a,b)
print(" ")

x = 0
y = 5.5
print("հասարակ իտերացիաների եղանակը")
print("համակարգը՝")
print()
print("լուծումը x=0 , y=5.5")
print(" ")
print("y = pow(x,2)+5")
print("y = 2*x+4")
basic_iteration_system_solver(x,y)


#print(" ")
#seccond(x)
#print(" ")
#third(x)
#print(" ")
#fourth(x)
#print(" ")
#x=float(-1.0) # first iteration X0 value
#a = -1
#b = 2
#x = -0.5

#if fixed_right_edge(b,x) == 0:
#    print("error right_edge")

#if combination(a,b) == 0:
#    print("error left edge")

#x = 0
#y = 5.5
#basic_iteration_system_solver(x,y)

#print(f_2(0))