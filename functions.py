import math
from constants import A, G, K_1, K_2, H_C, H_0, STEP

def adams_bashforth_3(t):
    if t == 0:
        return H_0
    else:
        q = H_0
        f_k = derivative(t - STEP, q)
        f_k1 = derivative(t - (2 * STEP), f_k)
        f_k2 = derivative(t - (3 * STEP), f_k1)
        return (H_0 + (STEP / 12) * (23 * f_k - 16 * f_k1 + 5 * f_k2))

# metodo de euler
# parametro: t (tiempo)
# retorna la altura del tanque en el tiempo t
def euler(t):
    steps = int(t / STEP)                       # cantidad de pasos a realizar
    q = H_0                                     # altura inicial del tanque
    for i in range(steps):
        q += STEP * derivative(i * STEP, q)     # calcula la altura en el tiempo t segun formula de Euler
    return q

# calcula la derivada dq(t)/dt en el tiempo t
# parametro: t (tiempo), q (altura del tanque, derivada en el tiempo t - STEP)
# es decir, la derivada de t se calcula en base a la derivada del tiempo anterior
def derivative(t, q):
    return ((1 / A) * f_input(t)) - ((1 / A) * f_output(t, q))

# calcula el caudal de salida del tanque segun la altura del agua en el tanque
# parametro: t (tiempo), q (altura del tanque, derivada en el tiempo t - STEP)
def f_output(t, q):
    if t == 0:
        return K_1 * math.sqrt(G * H_0)
    else:                                           # se calcula el caudal de salida del tiempo t, segun el valor de la derivada en t - STEP
        if q <= H_C:                                # si es menor a un valor critico la valvula se abre normal
            return K_1 * math.sqrt(G * q)
        else:                                       # si es mayor a un valor critico la valvula se abre mas de lo normal, saca mas caudal
            return (K_1 + K_2) * math.sqrt(G * q)

# calcula el caudal de entrada al tanque segun el tiempo
def f_input(t):
    return 15 + 5 * math.cos(0.1 * t)
