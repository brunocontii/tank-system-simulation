import math
from constants import A, G, K_1, K_2, H_C, H_0, STEP, SIM_TIME

def f_entrada(t):
    return 15 + 5 * math.cos(0.1 * t)

def f_salida(t):
    if t == 0:
        return K_1 * math.sqrt(G * H_0)
    else:
        if derivada(t) <= H_C:
            return K_1 * math.sqrt(G * derivada(t))
        else:
            return (K_1 + K_2) * math.sqrt(G * derivada(t))

def derivada(t):
    return ((1 / A) * f_entrada(t)) - ((1 / A) * f_salida(t))