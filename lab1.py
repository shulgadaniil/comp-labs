import numpy as np 
import matplotlib.pylab as plt

def evaluate(x_eval):   
    return x_eval*x_eval*f_a + x_eval*f_b + f_c

def check_integer(prompt, positive=True):
    while True:
        try:
            val = int(input(prompt))
            if positive and val < 0:
                print("Error - the input must be a positive integer number greater than zero - try again")
                continue
            if not positive and val > 0: 
                print("Error - the input must be a negative integer number less than zero - try again")
                continue
            return val
        except ValueError:
            print("Error - the input must be an integer (whole) number - try again")
        

f_a = float(input("input x squared coefficient: "))
f_b = float(input("input x coefficient: "))
f_c = float(input("input linear coefficient: "))
#range_1 = float(input("input x range start: "))
#range_2 = float(input("input x range end: "))

#x = np.arange(range_1, range_2, 0.02)

#if f_a != 0:
#    sqrt = np.sqrt(f_b*f_b -4*f_a*f_c)
#   print(f"discriminant: {round(sqrt, 3)}")
#    f_root_1 = (-(f_b)+sqrt)/(2*f_a)
#    print(f"root 1: {round(f_root_1, 3)}")
#    f_root_2 = (-(f_b)-sqrt)/(2*f_a)
#    print(f"root 2: {round(f_root_2, 3)}")
#    f_midpoint = (f_root_1 + f_root_2)/2
#    plt.plot(x, (x*0 + f_midpoint*f_midpoint*f_a + f_midpoint*f_b + f_c))
#    plt.scatter(f_midpoint, f_midpoint*f_midpoint*f_a + f_midpoint*f_b + f_c, color='blue')
#    plt.text(f_midpoint, (f_midpoint*f_midpoint*f_a + f_midpoint*f_b + f_c)*1.1, f"vertex({round(f_midpoint, 3)}, {round(f_midpoint*f_midpoint*f_a + f_midpoint*f_b + f_c, 3)})", fontsize=8, color='blue')
#    plt.scatter(f_root_1, f_root_1*f_root_1*f_a + f_root_1*f_b + f_c, color='green')
#    plt.scatter(f_root_2, f_root_2*f_root_2*f_a + f_root_2*f_b + f_c, color='green')

x_eval = float(input("find f(x) where x = "))
f_eval = evaluate(x_eval)
print(f"f({x_eval}) = {round(f_eval, 3)} to 3.d.p.")

#plt.plot(x, (f_a*x*x + f_b*x + f_c))
#plt.grid(True)
#plt.show()


print(f"FINDING ROOTS OF FUNCTION f(x) = {f_a}x^2 + {f_b}x + {f_c}")

x_1 = check_integer("input a value for x_1 < 0 : ", positive=False)

x_3 = check_integer("input a value for x_3 > 0 : ", positive=True)

x_2 = (x_1 + x_3)/2

tol = 0.0001
nsteps = 0

while True:
    f_2 = evaluate(x_2)
    if abs(evaluate(x_2)) < tol: 
        break
    if f_2 > 0:
        x_3 = x_2
    else: 
        x_1 = x_2
    x_2 = (x_1 + x_3)/2
    nsteps += 1


print(f"THE FUNCTION f(x) = 0 AT x = {round(x_2, 3)}        computed in {nsteps} manipulations")



##    