from constants import SIM_TIME, STEP
from functions import euler, adams_bashforth_3

steps = int(SIM_TIME / STEP) + 1

with open("euler_results.txt", "w") as euler_file, open ("adams_results.txt", "w") as adams_file:
    for i in range(steps):
        t = i * STEP
        euler_result = euler(t)
        adams_result = adams_bashforth_3(t)
        euler_file.write(f"{t:.2f} {euler_result:.5f}\n")
        adams_file.write(f"{t:.2f} {adams_result:.5f}\n")
        # para ponerlo lindo en forma de tabla
        print(f"t={t:.2f} | Euler: {euler_result:.5f} | Adams-Bashforth 3: {adams_result:.5f}")

