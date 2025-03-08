import numpy as np

def f(t, y):
    return t - y**2

def euler_method(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    y = y0
    t = t0

    for _ in range(n):
        y += h * f(t, y)
        t += h

    return y

def runge_kutta_4(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    y = y0
    t = t0

    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h

    return y

if __name__ == "__main__":
    t0 = 0
    y0 = 1
    t_end = 2
    n = 10

    euler_result = euler_method(f, t0, y0, t_end, n)
    rk4_result = runge_kutta_4(f, t0, y0, t_end, n)

    print(f"Euler Method Result: {euler_result}")
    print(f"Runge-Kutta Method Result: {rk4_result}")
