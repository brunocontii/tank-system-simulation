from constants import SIM_TIME, STEP
from functions import euler, adams_bashforth_3

steps = int(SIM_TIME / STEP) + 1
for i in range(steps):
    t = i * STEP
    euler_result = euler(t)
    adams_result = adams_bashforth_3(t)
    # para ponerlo lindo en forma de tabla
    print(f"t={t:.2f} | Euler: {euler_result:.5f} | Adams-Bashforth 3: {adams_result:.5f}")