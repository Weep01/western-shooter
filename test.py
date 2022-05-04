from math import cos
from math import sin
from math import tan
from math import radians
import matplotlib.pyplot as plt


global v0
global x
global ang

g = 9.8
h = 0
ang = 30
alpha = radians(ang)
v0 = 23
x_depart = 0
x = 0

def calc_ang():
    global alpha
    alpha = radians(ang)

x_data = []
y_data = []

def y(x):
    eq = (-1/2)*g*(((x-x_depart)**2)/( (v0**2)*(cos(alpha)**2)) ) + tan(alpha)*(x-x_depart)+h
    return eq

def rebond(x):
    x_data.append(x)
    y_data.append(y(x))
    print("x:{} y:{}".format(x, y(x)))
    return x, y(x)

def loop():
    global v0
    global x
    global x_depart
    global ang

    for i in range(1, 200):
        x_retrieved, y_retrieved = rebond(i)
        if x_retrieved > 1000:
            break
        if y_retrieved < 0:
            x_depart = x_retrieved
            v0/=1.1
            print(v0)
            if v0 < 5:
                break
            calc_ang()
            ang = ang / 1.2


loop()
        

plt.plot(x_data, y_data)
plt.show()