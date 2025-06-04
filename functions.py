import math
from constants import A, G, K_1, K_2, H_C, H_0, STEP

def adams_bashforth_3(t):
    if t == 0:
        return H_0
    else:
        f_k = derivative(t - STEP)
        f_k1 = derivative(t - (2 * STEP))
        f_k2 = derivative(t - (3 * STEP))
        return (H_0 + (STEP / 12) * (23 * f_k - 16 * f_k1 + 5 * f_k2))

def forward_euler(t):
    if t == 0:
        return H_0
    else:
        return forward_euler(t - STEP) + (STEP * (derivative(t - STEP)))

def f_input(t):
    return 15 + 5 * math.cos(0.1 * t)

def f_output(t):
    if t == 0:
        return K_1 * math.sqrt(G * H_0)
    else:
        if forward_euler(t - STEP) <= H_C:
            return K_1 * math.sqrt(G * forward_euler(t - STEP))
        else:
            return (K_1 + K_2) * math.sqrt(G * forward_euler(t - STEP))

def derivative(t):
    return ((1 / A) * f_input(t)) - ((1 / A) * f_output(t))