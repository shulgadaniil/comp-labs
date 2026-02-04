import numpy as np 
import matplotlib.pylab as plt

f_a = float(input("input x squared coefficient: "))
f_b = float(input("input x coefficient: "))
f_c = float(input("input linear coefficient: "))
print(f"function f(x) = {f_a}x^2 + {f_b}x + {f_c}")
range_1 = float(input("input x range start: "))
range_2 = float(input("input x range end: "))

x = np.arange(range_1, range_2, 0.02)

if f_a != 0:
    sqrt = np.sqrt(f_b*f_b -4*f_a*f_c)
    print(f"discriminant: {round(sqrt, 3)}")
    f_root_1 = (-(f_b)+sqrt)/(2*f_a)
    print(f"root 1: {round(f_root_1, 3)}")
    f_root_2 = (-(f_b)-sqrt)/(2*f_a)
    print(f"root 2: {round(f_root_2, 3)}")
    f_midpoint = (f_root_1 + f_root_2)/2
    plt.plot(x, (x*0 + f_midpoint*f_midpoint*f_a + f_midpoint*f_b + f_c))
    plt.scatter(f_midpoint, f_midpoint*f_midpoint*f_a + f_midpoint*f_b + f_c, color='blue')
    plt.text(f_midpoint, (f_midpoint*f_midpoint*f_a + f_midpoint*f_b + f_c)*1.1, f"vertex({round(f_midpoint, 3)}, {round(f_midpoint*f_midpoint*f_a + f_midpoint*f_b + f_c, 3)})", fontsize=8, color='blue')
    plt.scatter(f_root_1, f_root_1*f_root_1*f_a + f_root_1*f_b + f_c, color='green')
    plt.scatter(f_root_2, f_root_2*f_root_2*f_a + f_root_2*f_b + f_c, color='green')

x_eval = float(input("find f(..."))
f_eval = x_eval*x_eval*f_a + x_eval*f_b + f_c
print(f"f({x_eval}) = {round(f_eval, 3)}")


plt.plot(x, (f_a*x*x + f_b*x + f_c))
plt.grid(True)
plt.show()

x_1 = input("input a value <0 for x_1: ")
while type(x_1) != float or x_1 >= 0:
    print("invalid input, try again")
    x_1 = input("input a value <0 for x_1: ")
    else:
        break
    
x_3 = input("input a value >0 for x_3: ")
while type(x_3) == str or x_3 <= 0:
    print("invalid input, try again")
    x_1 = input("input a value <0 for x_1: ")

x_2 = (x_1 + x_3)/2

##    
