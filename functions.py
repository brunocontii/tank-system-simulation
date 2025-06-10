import math
from constants import A, G, K_1, K_2, H_C, H_0, STEP

# metodo de integracion numerica euler
# parametro: t (tiempo)
# retorna la altura del tanque en el tiempo t
def euler(t):
    steps = int(t / STEP)                       # cantidad de pasos a realizar
    q = H_0                                     # altura inicial del tanque
    for i in range(steps):
        q += STEP * derivative(i * STEP, q)     # calcula la altura en el tiempo t segun formula de Euler
    return q

# metodo de integracion numerica adams-bashforth de orden 3
# parametro: t (tiempo)
# necesito los 3 anteriores para calcular el siguiente paso
# por eso si el paso es 1 o 2 se usa el metodo de euler, para que no de error
# si los pasos son mayores a 2, se usa el metodo de adams-bashforth de orden 3
def adams_bashforth_3(t):
    steps = int(t / STEP)
    x = H_0
    
    if steps == 1:
        return euler(t)
    elif steps == 2:
        return euler(t)
    for i in range(2, steps):
        x += (STEP/12 * (23 * derivative((i - 2) * STEP, x) - 16 * derivative((i - 1) * STEP, x) + 5 * derivative(i * STEP, x)))
    return x


# derivada dq(t)/dt en el tiempo t
# parametros: t (tiempo), q (altura del tanque, derivada en el tiempo t - STEP)
# es decir, la derivada de t se calcula en base a la derivada del tiempo anterior
def derivative(t, q):
    return ((1 / A) * f_input(t)) - ((1 / A) * f_output(t, q))

# calcula el caudal de salida del tanque segun la altura del agua en el tanque
# parametros: t (tiempo), q (altura del tanque, derivada en el tiempo t - STEP)
def f_output(t, q):
    if t == 0:
        return K_1 * math.sqrt(G * H_0)
    else:                                           # se calcula el caudal de salida del tiempo t, segun el valor de la derivada en t - STEP
        if q <= H_C:                                # si es menor a un valor critico la valvula se abre normal
            return K_1 * math.sqrt(G * q)
        else:                                       # si es mayor a un valor critico la valvula se abre mas de lo normal, saca mas caudal
            return (K_1 + K_2) * math.sqrt(G * q)

# calcula el caudal de entrada al tanque segun el tiempo t
# parametro: t (tiempo)
def f_input(t):
    return 15 + 5 * math.cos(0.1 * t)